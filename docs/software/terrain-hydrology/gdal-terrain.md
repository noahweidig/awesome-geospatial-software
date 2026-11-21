---
title: "gdaldem"
icon: lucide/mountain
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/terrain-hydrology.yml
tags:
  - Windows
  - macOS
  - Linux
  - Command line
  - C++
  - Open source
  - Active
  - MIT
  - Terrain analysis
  - Raster
  - GDAL-based
  - OSGeo
---

# ![](../../assets/logos/gdal-terrain.png){ .title-logo } gdaldem

GDAL utility that computes hillshade, slope, aspect, roughness and color relief from a DEM.

[:lucide-download: Get the software](https://gdal.org/en/stable/programs/gdaldem.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://gdal.org/en/stable/programs/gdaldem.html){ .md-button }
[:lucide-code: Source code](https://github.com/OSGeo/gdal){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | OSGeo |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | C++ |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Command line"

    ```bash
    gdaldem hillshade dem.tif hillshade.tif -z 2 -compute_edges
    gdaldem slope dem.tif slope.tif -compute_edges
    ```


## Related software

- [GDAL](../core-libraries/gdal.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "gdaldem", "description": "GDAL utility that computes hillshade, slope, aspect, roughness and color relief from a DEM.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/terrain-hydrology/gdal-terrain/", "applicationCategory": "Terrain, hydrology & hazards", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["C++"], "author": {"@type": "Organization", "name": "OSGeo"}, "keywords": ["Windows", "macOS", "Linux", "Command line", "C++", "Open source", "Active", "MIT", "Terrain analysis", "Raster", "GDAL-based", "OSGeo"], "license": "MIT", "sameAs": "https://gdal.org/en/stable/programs/gdaldem.html", "downloadUrl": "https://gdal.org/en/stable/programs/gdaldem.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/gdal-terrain.png", "codeRepository": "https://github.com/OSGeo/gdal"}</script>

[:lucide-arrow-left: Back to Terrain, hydrology & hazards](index.md){ .md-button }
