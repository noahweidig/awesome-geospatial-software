---
title: "Cartopy"
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
  - BSD
  - Cartography
  - Visualization
  - Climate
  - Projections
---

# ![](../../assets/logos/cartopy.png){ .title-logo } Cartopy

Matplotlib-based mapping with projection support, transformations and Natural Earth feature layers for publication maps.

[:lucide-download: Get the software](https://cartopy.readthedocs.io/stable/installing.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://cartopy.readthedocs.io/){ .md-button }
[:lucide-code: Source code](https://github.com/SciTools/cartopy){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | SciTools |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | BSD-3-Clause |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import matplotlib.pyplot as plt, cartopy.crs as ccrs
    ax = plt.axes(projection=ccrs.Robinson())
    ax.coastlines(); ax.gridlines()
    plt.show()
    ```


## Related software

- [PyGMT](../python/pygmt.md)
- [GeoViews](../python/geoviews.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "Cartopy", "description": "Matplotlib-based mapping with projection support, transformations and Natural Earth feature layers for publication maps.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/cartopy/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "SciTools"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "Python", "Open source", "Active", "BSD", "Cartography", "Visualization", "Climate", "Projections"], "license": "BSD-3-Clause", "sameAs": "https://cartopy.readthedocs.io/", "downloadUrl": "https://cartopy.readthedocs.io/stable/installing.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/cartopy.png", "codeRepository": "https://github.com/SciTools/cartopy"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
