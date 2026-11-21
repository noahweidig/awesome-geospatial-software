---
title: "pyproj"
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
  - MIT
  - Projections
  - Geodesy
---

# ![](../../assets/logos/pyproj.png){ .title-logo } pyproj

Python interface to PROJ for coordinate reference system lookups, coordinate transformations and geodesic calculations.

[:lucide-download: Get the software](https://pyproj4.github.io/pyproj/stable/installation.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://pyproj4.github.io/pyproj/stable/){ .md-button }
[:lucide-code: Source code](https://github.com/pyproj4/pyproj){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | pyproj contributors |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    from pyproj import Transformer
    t = Transformer.from_crs("EPSG:4326", "EPSG:32610", always_xy=True)
    print(t.transform(-122.42, 37.77))
    ```


## Related software

- [PROJ](../core-libraries/proj.md)
- [GeoPandas](../python/geopandas.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "pyproj", "description": "Python interface to PROJ for coordinate reference system lookups, coordinate transformations and geodesic calculations.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/pyproj/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "pyproj contributors"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Command line", "Python", "Open source", "Active", "MIT", "Projections", "Geodesy"], "license": "MIT", "sameAs": "https://pyproj4.github.io/pyproj/stable/", "downloadUrl": "https://pyproj4.github.io/pyproj/stable/installation.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/pyproj.png", "codeRepository": "https://github.com/pyproj4/pyproj"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
