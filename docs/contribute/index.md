---
icon: lucide/git-pull-request
---

# Contribute

Software pages are generated from YAML in `data/software/`. Add an entry and open a pull request. Each edit button on a software page opens the generated file, so edit the YAML instead.

[:fontawesome-brands-github: Open the repository](https://github.com/noahweidig/awesome-geospatial-software){ .md-button .md-button--primary }
[:lucide-circle-alert: Suggest software](https://github.com/noahweidig/awesome-geospatial-software/issues/new?template=new-software.yml){ .md-button }

## Inclusion criteria

- Geospatial work is the main purpose, or a core feature (for example a database spatial extension).
- Users can get it publicly. Free registration, trials and commercial licenses are fine.
- The link goes to the developer, the official documentation or a stable package registry.
- Developer, platforms, license and cost can be stated from the source.

## Entry format

Add to the file for the matching category, for example `data/software/python.yml`:

```yaml
- id: my-tool               # unique, becomes the page URL
  title: My Tool (MT)       # text in parentheses is dropped in the navigation
  icon: lucide/file-code    # fallback icon when no logo is available
  summary: One sentence.
  provider: Organization or maintainer
  platform: [Windows, macOS, Linux]
  language: [Python]
  interface: [Library]
  license: MIT
  cost: Open source
  status: Active
  access: https://example.org/download
  docs: https://example.org/docs
  repo: https://github.com/example/my-tool
  tags: [MIT, Vector, Spatial join]
  caveat: Optional warning shown on the page.
```

`platform`, `interface`, `language`, `cost` and `status` become tags automatically. Add the license tag, topics and ecosystem to `tags`. All tags must exist in `data/tag-vocab.yml`. To add a tag, add it there under a category.

Optional fields:

- `repo`: source code link. Shown as a button and used by the logo and license checks.
- `doi`: bare DOI such as `10.1016/j.compenvurbsys.2017.05.004`. Shown under Cite and in the structured data.
- `citation`: preferred citation text.
- `verified`: `YYYY-MM-DD` date you last checked the entry against the developer. Shown in the table.
- `snippets`: list of `{label, lang, code}` shown as tabs under Quick start.
- `related`: list of `id` values for similar or complementary software.

`python scripts/validate.py` checks entries against `data/schema.json`. CI runs it on every pull request. See [CONTRIBUTING.md](https://github.com/noahweidig/awesome-geospatial-software/blob/main/CONTRIBUTING.md).

## Logos

Logos live in `docs/assets/logos/<id>.png`. Run `python scripts/fetch_logos.py <id>` to download one from the project's site, or add a square PNG by hand. Entries without a logo show their category icon. Logos are trademarks of their owners and appear only to identify the software.

## Build locally

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate.py
zensical serve
```
