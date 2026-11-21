---
title: "GeoPandas"
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
  - Vector
  - Spatial join
  - Overlay
  - Pangeo
---

# ![](../../assets/logos/geopandas.png){ .title-logo } GeoPandas

Pandas extension that adds geometry columns, spatial joins, overlays and file reading and writing for vector data.

[:lucide-download: Get the software](https://geopandas.org/en/stable/getting_started/install.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://geopandas.org/){ .md-button }
[:lucide-code: Source code](https://github.com/geopandas/geopandas){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | GeoPandas developers |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | BSD-3-Clause |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Install"

    ```bash
    pip install geopandas
    ```

=== "Read and join"

    ```python
    import geopandas as gpd
    counties = gpd.read_file("counties.gpkg")
    pts = gpd.read_file("points.geojson").to_crs(counties.crs)
    joined = gpd.sjoin(pts, counties, predicate="within")
    ```


## Related software

- [Shapely](../python/shapely.md)
- [pyogrio](../python/pyogrio.md)
- [pyproj](../python/pyproj.md)
- [sf](../r/sf.md)
- [dask-geopandas](../python/dask-geopandas.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "GeoPandas", "description": "Pandas extension that adds geometry columns, spatial joins, overlays and file reading and writing for vector data.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/geopandas/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "GeoPandas developers"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "Python", "Open source", "Active", "BSD", "Vector", "Spatial join", "Overlay", "Pangeo"], "license": "BSD-3-Clause", "sameAs": "https://geopandas.org/", "downloadUrl": "https://geopandas.org/en/stable/getting_started/install.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/geopandas.png", "codeRepository": "https://github.com/geopandas/geopandas"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
