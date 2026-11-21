---
title: "pystac-client"
icon: lucide/file-code
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/python.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - Command line
  - Python
  - Open source
  - Active
  - Apache-2.0
  - STAC
  - Data catalog
  - Satellite imagery
---

# ![](../../assets/logos/pystac-client.png){ .title-logo } pystac-client

Python client for searching STAC APIs, used with Microsoft Planetary Computer, Earth Search and other catalogs.

[:lucide-download: Get the software](https://pystac-client.readthedocs.io/en/stable/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://pystac-client.readthedocs.io/){ .md-button }
[:lucide-code: Source code](https://github.com/stac-utils/pystac-client){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | STAC community |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Apache-2.0 |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    from pystac_client import Client
    cat = Client.open("https://earth-search.aws.element84.com/v1")
    items = cat.search(collections=["sentinel-2-l2a"], bbox=[-122.6, 37.6, -122.3, 37.9],
                       datetime="2025-06-01/2025-06-30").item_collection()
    print(len(items))
    ```


## Related software

- [PySTAC](../python/pystac.md)
- [odc-stac](../python/odc-stac.md)
- [stackstac](../python/stackstac.md)
- [planetary-computer](../python/planetary-computer.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "pystac-client", "description": "Python client for searching STAC APIs, used with Microsoft Planetary Computer, Earth Search and other catalogs.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/pystac-client/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "STAC community"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Command line", "Python", "Open source", "Active", "Apache-2.0", "STAC", "Data catalog", "Satellite imagery"], "license": "Apache-2.0", "sameAs": "https://pystac-client.readthedocs.io/", "downloadUrl": "https://pystac-client.readthedocs.io/en/stable/", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/pystac-client.png", "codeRepository": "https://github.com/stac-utils/pystac-client"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
