---
title: "Shapely"
icon: lucide/file-code
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/python.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - Python
  - C
  - Open source
  - Active
  - BSD
  - Vector
  - Overlay
---

# Shapely

Python package for creating and manipulating planar geometries, built on GEOS with vectorized operations on NumPy arrays.

[:lucide-download: Get the software](https://shapely.readthedocs.io/en/stable/installation.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://shapely.readthedocs.io/){ .md-button }
[:lucide-code: Source code](https://github.com/shapely/shapely){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Shapely contributors |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python, C |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | BSD-3-Clause |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    from shapely.geometry import Point
    buf = Point(0, 0).buffer(10)
    print(buf.area, buf.contains(Point(3, 4)))
    ```


## Related software

- [GEOS](../core-libraries/geos.md)
- [GeoPandas](../python/geopandas.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "Shapely", "description": "Python package for creating and manipulating planar geometries, built on GEOS with vectorized operations on NumPy arrays.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/shapely/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python", "C"], "author": {"@type": "Organization", "name": "Shapely contributors"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Python", "C", "Open source", "Active", "BSD", "Vector", "Overlay"], "license": "BSD-3-Clause", "sameAs": "https://shapely.readthedocs.io/", "downloadUrl": "https://shapely.readthedocs.io/en/stable/installation.html", "codeRepository": "https://github.com/shapely/shapely"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
