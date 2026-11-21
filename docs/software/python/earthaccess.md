---
title: "earthaccess"
icon: lucide/file-code
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/python.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - Notebook
  - Python
  - Open source
  - Active
  - MIT
  - Earth observation
  - Satellite imagery
  - NASA
---

# ![](../../assets/logos/earthaccess.png){ .title-logo } earthaccess

Python library to search, download and stream NASA Earthdata products with Earthdata Login authentication.

[:lucide-download: Get the software](https://earthaccess.readthedocs.io/en/stable/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://earthaccess.readthedocs.io/){ .md-button }
[:lucide-code: Source code](https://github.com/nsidc/earthaccess){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | earthaccess developers |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import earthaccess
    earthaccess.login()
    results = earthaccess.search_data(short_name="HLSL30", bounding_box=(-122.6, 37.6, -122.3, 37.9),
                                      temporal=("2025-06-01", "2025-06-30"))
    files = earthaccess.download(results, "data/")
    ```


## Related software

- [pystac-client](../python/pystac-client.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "earthaccess", "description": "Python library to search, download and stream NASA Earthdata products with Earthdata Login authentication.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/earthaccess/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "earthaccess developers"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "Python", "Open source", "Active", "MIT", "Earth observation", "Satellite imagery", "NASA"], "license": "MIT", "sameAs": "https://earthaccess.readthedocs.io/", "downloadUrl": "https://earthaccess.readthedocs.io/en/stable/", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/earthaccess.png", "codeRepository": "https://github.com/nsidc/earthaccess"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
