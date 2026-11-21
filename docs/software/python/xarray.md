---
title: "xarray"
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
  - Climate
  - Time series
  - Pangeo
---

# xarray

Labeled multi-dimensional arrays for NetCDF, Zarr and GRIB data, the base of the Pangeo geoscience stack.

[:lucide-download: Get the software](https://docs.xarray.dev/en/stable/getting-started-guide/installing.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://docs.xarray.dev/){ .md-button }
[:lucide-code: Source code](https://github.com/pydata/xarray){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | xarray developers |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Apache-2.0 |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import xarray as xr
    ds = xr.open_dataset("temp.nc")
    print(ds["t2m"].mean("time"))
    ```


## Related software

- [rioxarray](../python/rioxarray.md)
- [dask-geopandas](../python/dask-geopandas.md)
- [stackstac](../python/stackstac.md)
- [odc-stac](../python/odc-stac.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "xarray", "description": "Labeled multi-dimensional arrays for NetCDF, Zarr and GRIB data, the base of the Pangeo geoscience stack.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/xarray/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "xarray developers"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "Python", "Open source", "Active", "Apache-2.0", "Raster", "Climate", "Time series", "Pangeo"], "license": "Apache-2.0", "sameAs": "https://docs.xarray.dev/", "downloadUrl": "https://docs.xarray.dev/en/stable/getting-started-guide/installing.html", "codeRepository": "https://github.com/pydata/xarray"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
