#!/usr/bin/env python3
"""Validate data/*.yml against data/schema.json and cross-file rules."""
import importlib.util
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
VOCAB_FIELDS = {"platform": "platform", "interface": "interface", "language": "language",
                "cost": "cost", "status": "status"}


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def read_entries(validator, slugs, errors):
    """Return [(filename, entry)] and a map of id -> filename."""
    entries, ids = [], {}
    for f in sorted((ROOT / "data" / "software").glob("*.yml")):
        if f.stem not in slugs:
            errors.append(f"{f.name}: no theme with slug {f.stem!r} in data/themes.yml")
        data = load(f) or []
        for err in validator.iter_errors(data):
            path = "/".join(str(p) for p in err.absolute_path)
            errors.append(f"{f.name}: {path}: {err.message}")
        if not isinstance(data, list):
            continue
        for e in (e for e in data if isinstance(e, dict)):
            if e.get("id") in ids:
                errors.append(f"{f.name}: duplicate id {e['id']!r} (also in {ids[e['id']]})")
            ids[e.get("id")] = f.name
            entries.append((f.name, e))
    return entries, ids


def icon_names():
    spec = importlib.util.find_spec("zensical_ui")
    if not spec or not spec.submodule_search_locations:
        return None
    d = Path(list(spec.submodule_search_locations)[0]) / "templates" / ".icons" / "lucide"
    return {p.stem for p in d.glob("*.svg")} if d.exists() else None


def check_entry(name, e, vocab, ids, icons, errors):
    allowed = {t for v in vocab.values() for t in v["tags"]}
    for t in e.get("tags", []):
        if t not in allowed:
            errors.append(f"{name}: {e['id']}: tag {t!r} not in data/tag-vocab.yml")
    for field, cat in VOCAB_FIELDS.items():
        vals = e.get(field)
        for v in vals if isinstance(vals, list) else [vals]:
            if v is not None and v not in vocab[cat]["tags"]:
                errors.append(f"{name}: {e['id']}: {field} {v!r} not in data/tag-vocab.yml ({cat})")
    for r in e.get("related", []):
        if r not in ids:
            errors.append(f"{name}: {e['id']}: related id {r!r} does not exist")
        elif r == e["id"]:
            errors.append(f"{name}: {e['id']}: related lists itself")
    if icons is not None and e.get("icon", "").split("/")[-1] not in icons:
        errors.append(f"{name}: {e['id']}: unknown Lucide icon {e.get('icon')!r}")


def main():
    schema = json.loads((ROOT / "data" / "schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    themes = load(ROOT / "data" / "themes.yml")
    slugs = {t["slug"] for t in themes}
    vocab = load(ROOT / "data" / "tag-vocab.yml")
    icons = icon_names()
    errors = []
    seen = {}
    for cat, v in vocab.items():
        for tag in v["tags"]:
            if tag in seen:
                errors.append(f"data/tag-vocab.yml: tag {tag!r} is in both {seen[tag]!r} and {cat!r}")
            seen[tag] = cat
    for t in themes:
        if icons is not None and t["icon"].split("/")[-1] not in icons:
            errors.append(f"themes.yml: {t['slug']}: unknown Lucide icon {t['icon']!r}")
    entries, ids = read_entries(validator, slugs, errors)
    for name, e in entries:
        check_entry(name, e, vocab, ids, icons, errors)
    if errors:
        sys.exit("\n".join(errors))
    print(f"ok: {len(entries)} entries in {len(slugs)} themes")


if __name__ == "__main__":
    main()
