---
title: "PySAL"
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
  - Spatial statistics
  - Hotspot analysis
  - PySAL
---

# ![](../../assets/logos/pysal.png){ .title-logo } PySAL

Family of Python packages for spatial analysis, including libpysal, esda, spreg, mgwr, spopt, segregation and tobler.

[:lucide-download: Get the software](https://pysal.org/pysal/installation.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://pysal.org/){ .md-button }
[:lucide-code: Source code](https://github.com/pysal/pysal){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | PySAL developers |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | BSD-3-Clause |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import geopandas as gpd
    from libpysal import weights
    from esda.moran import Moran
    gdf = gpd.read_file("tracts.gpkg")
    w = weights.Queen.from_dataframe(gdf); w.transform = "r"
    print(Moran(gdf["income"], w).I)
    ```


## Related software

- [GeoDa](../spatial-analysis/geoda.md)
- [spdep](../r/spdep.md)
- [momepy](../python/momepy.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "PySAL", "description": "Family of Python packages for spatial analysis, including libpysal, esda, spreg, mgwr, spopt, segregation and tobler.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/pysal/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "PySAL developers"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "Python", "Open source", "Active", "BSD", "Spatial statistics", "Hotspot analysis", "PySAL"], "license": "BSD-3-Clause", "sameAs": "https://pysal.org/", "downloadUrl": "https://pysal.org/pysal/installation.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/pysal.png", "codeRepository": "https://github.com/pysal/pysal"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
