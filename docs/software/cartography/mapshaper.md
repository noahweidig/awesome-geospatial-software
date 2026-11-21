---
title: "Mapshaper"
icon: lucide/palette
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/cartography.yml
tags:
  - Web browser
  - Windows
  - macOS
  - Linux
  - Web app
  - Command line
  - JavaScript
  - Open source
  - Active
  - MPL
  - Cartography
  - Vector
  - ETL
---

# Mapshaper

Editor and command line tool for simplifying, clipping, dissolving and converting polygon, line and point data, with a browser interface.

[:lucide-download: Get the software](https://mapshaper.org/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://github.com/mbloch/mapshaper/wiki){ .md-button }
[:lucide-code: Source code](https://github.com/mbloch/mapshaper){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Matthew Bloch |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Web browser, Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | JavaScript |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Web app, Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MPL-2.0 |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Command line"

    ```bash
    mapshaper counties.shp -simplify 10% -o counties_simple.geojson format=geojson
    ```


## Related software

- [D3](../web-mapping/d3-geo.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "Mapshaper", "description": "Editor and command line tool for simplifying, clipping, dissolving and converting polygon, line and point data, with a browser interface.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/cartography/mapshaper/", "applicationCategory": "Cartography & visualization", "operatingSystem": "Web browser, Windows, macOS, Linux", "programmingLanguage": ["JavaScript"], "author": {"@type": "Organization", "name": "Matthew Bloch"}, "keywords": ["Web browser", "Windows", "macOS", "Linux", "Web app", "Command line", "JavaScript", "Open source", "Active", "MPL", "Cartography", "Vector", "ETL"], "license": "MPL-2.0", "sameAs": "https://github.com/mbloch/mapshaper/wiki", "downloadUrl": "https://mapshaper.org/", "codeRepository": "https://github.com/mbloch/mapshaper"}</script>

[:lucide-arrow-left: Back to Cartography & visualization](index.md){ .md-button }
