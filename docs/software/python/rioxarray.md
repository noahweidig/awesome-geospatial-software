---
title: "rioxarray"
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
  - Apache-2.0
  - Raster
  - Pangeo
---

# rioxarray

Adds rasterio-based CRS handling, reprojection, clipping and GeoTIFF I/O to xarray objects.

[:lucide-download: Get the software](https://vylor.github.io/rioxarray/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://vylor.github.io/rioxarray/){ .md-button }
[:lucide-code: Source code](https://github.com/vylor/rioxarray){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | rioxarray contributors |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Apache-2.0 |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import rioxarray
    da = rioxarray.open_rasterio("dem.tif", masked=True)
    da.rio.reproject("EPSG:3857").rio.to_raster("dem_3857.tif")
    ```


## Related software

- [xarray](../python/xarray.md)
- [rasterio](../python/rasterio.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "rioxarray", "description": "Adds rasterio-based CRS handling, reprojection, clipping and GeoTIFF I/O to xarray objects.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/rioxarray/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "rioxarray contributors"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "Python", "Open source", "Active", "Apache-2.0", "Raster", "Pangeo"], "license": "Apache-2.0", "sameAs": "https://vylor.github.io/rioxarray/", "downloadUrl": "https://vylor.github.io/rioxarray/", "codeRepository": "https://github.com/vylor/rioxarray"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
