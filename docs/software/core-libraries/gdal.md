---
title: "GDAL"
icon: lucide/library
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/core-libraries.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - Command line
  - C++
  - C
  - Python
  - Open source
  - Active
  - MIT
  - Raster
  - Vector
  - Cloud-native
  - OSGeo
---

# ![](../../assets/logos/gdal.png){ .title-logo } GDAL

The translator library for raster and vector geospatial formats, with the gdal and ogr2ogr command line tools and bindings for Python, Java, C# and others.

[:lucide-download: Get the software](https://gdal.org/en/stable/download.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://gdal.org/en/stable/){ .md-button }
[:lucide-code: Source code](https://github.com/OSGeo/gdal){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | OSGeo |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | C++, C, Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Command line"

    ```bash
    gdalinfo dem.tif
    ogr2ogr -f GPKG out.gpkg in.shp
    gdalwarp -t_srs EPSG:4326 in.tif out.tif
    ```

=== "Python"

    ```python
    from osgeo import gdal
    ds = gdal.Open("dem.tif")
    print(ds.RasterXSize, ds.RasterYSize, ds.GetProjection()[:40])
    ```


## Related software

- [PROJ](../core-libraries/proj.md)
- [GEOS](../core-libraries/geos.md)
- [rasterio](../python/rasterio.md)
- [pyogrio](../python/pyogrio.md)
- [terra](../r/terra.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "GDAL", "description": "The translator library for raster and vector geospatial formats, with the gdal and ogr2ogr command line tools and bindings for Python, Java, C# and others.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/core-libraries/gdal/", "applicationCategory": "Core libraries & engines", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["C++", "C", "Python"], "author": {"@type": "Organization", "name": "OSGeo"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Command line", "C++", "C", "Python", "Open source", "Active", "MIT", "Raster", "Vector", "Cloud-native", "OSGeo"], "license": "MIT", "sameAs": "https://gdal.org/en/stable/", "downloadUrl": "https://gdal.org/en/stable/download.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/gdal.png", "codeRepository": "https://github.com/OSGeo/gdal"}</script>

[:lucide-arrow-left: Back to Core libraries & engines](index.md){ .md-button }
