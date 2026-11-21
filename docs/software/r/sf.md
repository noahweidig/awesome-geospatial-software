---
title: "sf"
icon: lucide/sigma
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/r.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - R
  - C++
  - Open source
  - Active
  - GPL
  - MIT
  - Vector
  - Overlay
  - r-spatial
---

# ![](../../assets/logos/sf.png){ .title-logo } sf

Simple Features for R. Stores vector data as data frames with geometry columns and wraps GDAL, GEOS, PROJ and s2 for spatial operations.

[:lucide-download: Get the software](https://cran.r-project.org/package=sf){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://r-spatial.github.io/sf/){ .md-button }
[:lucide-code: Source code](https://github.com/r-spatial/sf){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Edzer Pebesma and r-spatial |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | R, C++ |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | GPL-2.0 or MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "R"

    ```r
    library(sf)
    nc <- st_read(system.file("shape/nc.shp", package = "sf"))
    nc_utm <- st_transform(nc, 32617)
    st_area(nc_utm[1, ])
    ```


## Related software

- [stars](../r/stars.md)
- [terra](../r/terra.md)
- [GeoPandas](../python/geopandas.md)
- [s2](../r/s2-r.md)
- [lwgeom](../r/lwgeom.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "sf", "description": "Simple Features for R. Stores vector data as data frames with geometry columns and wraps GDAL, GEOS, PROJ and s2 for spatial operations.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/r/sf/", "applicationCategory": "R packages", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["R", "C++"], "author": {"@type": "Organization", "name": "Edzer Pebesma and r-spatial"}, "keywords": ["Windows", "macOS", "Linux", "Library", "R", "C++", "Open source", "Active", "GPL", "MIT", "Vector", "Overlay", "r-spatial"], "license": "GPL-2.0 or MIT", "sameAs": "https://r-spatial.github.io/sf/", "downloadUrl": "https://cran.r-project.org/package=sf", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/sf.png", "codeRepository": "https://github.com/r-spatial/sf"}</script>

[:lucide-arrow-left: Back to R packages](index.md){ .md-button }
