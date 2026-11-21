# Contributing

Software pages are generated from YAML. Edit `data/software/<category>.yml`, not files under `docs/software/`.

## Add software

1. Pick the category file in `data/software/`. If none fits, add a category to `data/themes.yml` and a new file with the same slug.
2. Add an entry. Fields are listed in the [Contribute page](docs/contribute/index.md) and enforced by `data/schema.json`.
3. Tags must exist in `data/tag-vocab.yml`.
4. Use `related` to link similar software by `id`.
5. Optionally add a logo with `python scripts/fetch_logos.py <id>`.
6. Run the checks:

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate.py
zensical build --clean
```

## Inclusion criteria

- Geospatial work is the main purpose or a core feature.
- Users can get it publicly. Free, commercial and trial software are all fine.
- Links go to the developer, the official documentation or a stable package registry.
- Developer, platforms, license and cost are stated in the source.

## Accuracy

Every field must come from the developer or the project repository. Put unknowns in `caveat` or leave the software out. Do not copy values from other catalogs. Do not state prices or version numbers that go stale.

See the [Code of Conduct](CODE_OF_CONDUCT.md).
