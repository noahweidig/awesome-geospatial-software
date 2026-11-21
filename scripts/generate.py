#!/usr/bin/env python3
"""Generate software pages, theme indexes, tag config, hero and nav from data/*.yml."""
import csv
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://noahweidig.github.io/awesome-geospatial-software/"
EDIT = "https://github.com/noahweidig/awesome-geospatial-software/edit/main/"
REQUIRED = ["id", "title", "icon", "summary", "provider", "platform", "language", "interface",
            "license", "cost", "status", "access", "docs", "tags"]
DERIVED = ["platform", "interface", "language", "cost", "status"]


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def short(title):
    return re.sub(r"\s*\(.*?\)", "", title).strip()


def sc(icon):
    """lucide/globe -> :lucide-globe:"""
    return ":" + icon.replace("/", "-") + ":"


def q(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def yq(s):
    return '"' + q(s) + '"'


def replace_block(path, begin, end, body):
    text = path.read_text(encoding="utf-8")
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        sys.exit(f"markers {begin!r} not found in {path}")
    path.write_text(pat.sub(lambda _: f"{begin}\n{body}\n{end}", text), encoding="utf-8")


def logo_for(e):
    """Relative path under docs/ when a normalized logo exists for the entry."""
    return f"assets/logos/{e['id']}.png" if (DOCS / "assets" / "logos" / f"{e['id']}.png").exists() else None


def all_tags(e):
    """Explicit tags plus tags derived from platform, interface, language, cost and status."""
    out = []
    for v in [*e["platform"], *e["interface"], *e["language"], e["cost"], e["status"], *e["tags"]]:
        if v not in out:
            out.append(v)
    return out


def main():
    themes = load(ROOT / "data" / "themes.yml")
    vocab = load(ROOT / "data" / "tag-vocab.yml")
    tag_cat = {t: c for c, v in vocab.items() for t in v["tags"]}
    errors = []
    by_theme = {}
    ids = set()
    for th in themes:
        f = ROOT / "data" / "software" / f"{th['slug']}.yml"
        entries = load(f) if f.exists() else []
        for e in entries:
            for k in REQUIRED:
                if not e.get(k):
                    errors.append(f"{e.get('id', '?')}: missing {k}")
            if e["id"] in ids:
                errors.append(f"duplicate id {e['id']}")
            ids.add(e["id"])
            for t in all_tags(e):
                if t not in tag_cat:
                    errors.append(f"{e['id']}: tag {t!r} not in data/tag-vocab.yml")
        by_theme[th["slug"]] = sorted(entries, key=lambda e: e["title"].lower())
    if errors:
        sys.exit("\n".join(errors))

    dsroot = DOCS / "software"
    where = {e["id"]: (th["slug"], e) for th in themes for e in by_theme[th["slug"]]}
    for th in themes:
        d = dsroot / th["slug"]
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()
        entries = by_theme[th["slug"]]
        cards = []
        for e in entries:
            mark = f"![](../../{logo_for(e)}){{ .logo .middle }}" if logo_for(e) else f"{sc(e['icon'])}{{ .lg .middle }}"
            cards.append(
                f"-   {mark} __[{short(e['title'])}]({e['id']}.md)__\n\n"
                f"    ---\n\n    {e['summary']}\n\n"
                f"    [:lucide-arrow-right: Details]({e['id']}.md)"
            )
        (d / "index.md").write_text(
            f"---\nicon: {th['icon']}\nedit_url: {EDIT}data/themes.yml\n---\n\n# {th['title']}\n\n{th['summary']}\n\n"
            f"<div class=\"grid cards\" markdown>\n\n" + "\n\n".join(cards) + "\n\n</div>\n",
            encoding="utf-8")
        for e in entries:
            fm_tags = "\n".join(f"  - {t}" for t in all_tags(e))
            rows = [
                ("lucide-building-2", "Who develops or maintains the software", "Developer", e["provider"]),
                ("lucide-monitor-smartphone", "Operating systems and delivery", "Platforms", ", ".join(e["platform"])),
                ("lucide-code-xml", "Implementation or scripting languages", "Languages", ", ".join(e["language"])),
                ("lucide-mouse-pointer-click", "How you use it", "Interface", ", ".join(e["interface"])),
                ("lucide-scale", "Terms of use. Check the provider before redistributing", "License", e["license"]),
                ("lucide-circle-dollar-sign", "What it costs to use", "Cost", e["cost"]),
                ("lucide-activity", "Development state when the entry was written", "Status", e["status"]),
            ]
            if e.get("verified"):
                rows.append(("lucide-badge-check", "Date this entry was last checked against the provider", "Last verified", e["verified"]))
            table = "| Field | Value |\n| --- | --- |\n" + "\n".join(
                f"| :{i}:{{ title=\"{t}\" }} {lab} | {val} |" for i, t, lab, val in rows)
            rel = ""
            if e.get("related"):
                items = "\n".join(
                    f"- [{short(where[r][1]['title'])}](../{where[r][0]}/{r}.md)" for r in e["related"])
                rel = f"\n## Related software\n\n{items}\n"
            cite = ""
            if e.get("citation") or e.get("doi"):
                cite = "\n## Cite\n\n"
                if e.get("citation"):
                    cite += f"{e['citation']}\n\n"
                if e.get("doi"):
                    cite += f"DOI: [{e['doi']}](https://doi.org/{e['doi']})\n"
            snip = ""
            if e.get("snippets"):
                snip = "\n## Quick start\n\n"
                for s in e["snippets"]:
                    body = "\n".join("    " + ln if ln else "" for ln in s["code"].rstrip("\n").split("\n"))
                    snip += f'=== "{s["label"]}"\n\n    ```{s["lang"]}\n{body}\n    ```\n\n'
            ld = {"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": e["title"],
                  "description": e["summary"], "url": f"{SITE}software/{th['slug']}/{e['id']}/",
                  "applicationCategory": th["title"], "operatingSystem": ", ".join(e["platform"]),
                  "programmingLanguage": e["language"],
                  "author": {"@type": "Organization", "name": e["provider"]},
                  "keywords": all_tags(e), "license": e["license"], "sameAs": e["docs"],
                  "downloadUrl": e["access"]}
            if logo_for(e):
                ld["image"] = SITE + logo_for(e)
            if e.get("repo"):
                ld["codeRepository"] = e["repo"]
            if e.get("doi"):
                ld["identifier"] = f"https://doi.org/{e['doi']}"
            ldjs = json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")
            ldtag = f'\n<script type="application/ld+json">{ldjs}</script>\n'
            cav = f"\n!!! warning \"Caveat\"\n\n    {e['caveat']}\n" if e.get("caveat") else ""
            src = f"[:lucide-code: Source code]({e['repo']}){{ .md-button }}\n" if e.get("repo") else ""
            (d / f"{e['id']}.md").write_text(
                f"---\ntitle: {yq(e['title'])}\nicon: {e['icon']}\nedit_url: {EDIT}data/software/{th['slug']}.yml\ntags:\n{fm_tags}\n---\n\n"
                f"# {(f'![](../../{logo_for(e)}){{ .title-logo }} ') if logo_for(e) else ''}{e['title']}\n\n{e['summary']}\n\n"
                f"[:lucide-download: Get the software]({e['access']}){{ .md-button .md-button--primary }}\n"
                f"[:lucide-book-open: Documentation]({e['docs']}){{ .md-button }}\n{src}\n"
                f"## At a glance\n\n{table}\n{cav}{snip}{cite}{rel}{ldtag}\n"
                f"[:lucide-arrow-left: Back to {th['title']}](index.md){{ .md-button }}\n",
                encoding="utf-8")

    theme_cards = "\n\n".join(
        f"-   {sc(th['icon'])}{{ .lg .middle }} __[{th['title']}](software/{th['slug']}/index.md)__\n\n"
        f"    ---\n\n    {th['summary']}\n\n"
        f"    {len(by_theme[th['slug']])} tools\n\n"
        f"    [:lucide-arrow-right: Explore](software/{th['slug']}/index.md)"
        for th in themes)
    block = f"<div class=\"grid cards\" markdown>\n\n{theme_cards}\n\n</div>"
    replace_block(DOCS / "index.md", "<!-- BEGIN THEMES -->", "<!-- END THEMES -->", block)
    n = len(themes)
    orbs = "\n".join(
        f'<a class="orb" style="--i:{i};--n:{n}" href="software/{th["slug"]}/" title="{th["title"].replace("&", "&amp;")}" markdown>{sc(th["icon"])}</a>'
        for i, th in enumerate(themes))
    replace_block(DOCS / "index.md", "<!-- BEGIN ORBS -->", "<!-- END ORBS -->", orbs)
    total = sum(len(v) for v in by_theme.values())
    ds_block = block.replace("(software/", "(")
    (dsroot / "index.md").write_text(
        "---\nicon: lucide/layers\nedit_url: " + EDIT + "scripts/generate.py\n---\n\n# Software\n\n"
        f"{total} tools in {n} categories cover the geospatial landscape. Each page lists developer, platforms, "
        "languages, license, cost and where to get the software.\n\n"
        "<!-- BEGIN THEMES -->\n" + ds_block + "\n<!-- END THEMES -->\n", encoding="utf-8")

    th_title = {t["slug"]: t["title"] for t in themes}
    rows = []
    for th in themes:
        for e in by_theme[th["slug"]]:
            rows.append(
                f"| [{short(e['title'])}](../software/{th['slug']}/{e['id']}.md) | {th_title[th['slug']]} "
                f"| {', '.join(e['platform'])} | {', '.join(e['language'])} | {e['license']} | {e['cost']} |")
    (DOCS / "browse" / "all-software.md").write_text(
        "---\nicon: lucide/table\nedit_url: " + EDIT + "scripts/generate.py\nhide:\n  - tags\n---\n\n# All software\n\n"
        f"{total} tools. Click a column header to sort. Type to filter.\n\n"
        '<input type="search" id="dataset-filter" class="dataset-filter" placeholder="Filter software" aria-label="Filter software">\n\n'
        '<div class="sortable" markdown>\n\n'
        "| Software | Category | Platforms | Languages | License | Cost |\n| --- | --- | --- | --- | --- | --- |\n"
        + "\n".join(rows) + "\n\n</div>\n", encoding="utf-8")

    cat = []
    for th in themes:
        for e in by_theme[th["slug"]]:
            cat.append({"id": e["id"], "category": th["title"], "url": f"{SITE}software/{th['slug']}/{e['id']}/",
                        **{k: e[k] for k in e if k not in ("icon", "tags")}, "tags": all_tags(e)})
    out = DOCS / "assets"
    out.mkdir(parents=True, exist_ok=True)
    (out / "catalog.json").write_text(json.dumps(cat, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    cols = ["id", "title", "category", "provider", "platform", "language", "interface", "license", "cost",
            "status", "access", "docs", "repo", "doi", "verified", "url", "tags"]
    with open(out / "catalog.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for c in cat:
            w.writerow([";".join(c[k]) if isinstance(c.get(k), list) else c.get(k, "") for k in cols])

    nav_items = ['  { "Home" = "index.md" },']
    ds = ['      "software/index.md",']
    for th in themes:
        sub = [f'          "software/{th["slug"]}/index.md",']
        sub += [f'          {{ "{q(short(e["title"]))}" = "software/{th["slug"]}/{e["id"]}.md" }},'
                for e in by_theme[th["slug"]]]
        ds.append(f'      {{ "{q(th["title"])}" = [\n' + "\n".join(sub) + "\n      ] },")
    nav_items.append('  { "Software" = [\n' + "\n".join(ds) + "\n  ] },")
    nav_items.append('  { "Browse" = ["browse/index.md", "browse/all-software.md", "browse/tags.md"] },')
    nav_items.append('  { "Learn" = ["learn/index.md", "learn/choosing-software.md", "learn/geospatial-primer.md", "learn/open-source-stack.md", '
                     '"learn/compare-software.md", "learn/data-formats.md", "learn/data-sources.md", "learn/learning-resources.md", "learn/glossary.md"] },')
    nav_items.append('  { "Contribute" = ["contribute/index.md"] },')
    nav_items.append('  { "About" = ["about/index.md", "about/changelog.md"] },')
    replace_block(ROOT / "zensical.toml", "# BEGIN GENERATED NAV", "# END GENERATED NAV",
                  "nav = [\n" + "\n".join(nav_items) + "\n]")

    used = {t for ents in by_theme.values() for e in ents for t in all_tags(e)}
    ident, icons = [], ["default = \"lucide/hash\""]
    for c, v in vocab.items():
        icons.append(f'{c} = "{v["icon"]}"')
        ident += [f'"{q(t)}" = "{c}"' for t in v["tags"] if t in used]
    replace_block(ROOT / "zensical.toml", "# BEGIN GENERATED TAGS", "# END GENERATED TAGS",
                  "[project.extra.tags]\n" + "\n".join(ident) + "\n\n[project.theme.icon.tag]\n" + "\n".join(icons))
    print(f"generated {total} software pages in {len(themes)} themes")


if __name__ == "__main__":
    main()
