---
title: "rasterio"
icon: lucide/file-code
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/python.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - Command line
  - Python
  - Cython
  - Open source
  - Active
  - BSD
  - Raster
  - Cloud-native
---

# rasterio

Pythonic raster I/O built on GDAL that reads and writes GeoTIFF and other formats as NumPy arrays, with warping, masking and windowed reads.

[:lucide-download: Get the software](https://rasterio.readthedocs.io/en/stable/installation.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://rasterio.readthedocs.io/){ .md-button }
[:lucide-code: Source code](https://github.com/rasterio/rasterio){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Rasterio contributors |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python, Cython |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | BSD-3-Clause |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import rasterio
    with rasterio.open("dem.tif") as src:
        band = src.read(1, masked=True)
        print(src.crs, src.res, band.mean())
    ```


## Related software

- [GDAL](../core-libraries/gdal.md)
- [rioxarray](../python/rioxarray.md)
- [rio-cogeo](../python/rio-cogeo.md)
- [terra](../r/terra.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "rasterio", "description": "Pythonic raster I/O built on GDAL that reads and writes GeoTIFF and other formats as NumPy arrays, with warping, masking and windowed reads.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/rasterio/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python", "Cython"], "author": {"@type": "Organization", "name": "Rasterio contributors"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Command line", "Python", "Cython", "Open source", "Active", "BSD", "Raster", "Cloud-native"], "license": "BSD-3-Clause", "sameAs": "https://rasterio.readthedocs.io/", "downloadUrl": "https://rasterio.readthedocs.io/en/stable/installation.html", "codeRepository": "https://github.com/rasterio/rasterio"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
