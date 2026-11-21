---
icon: lucide/git-compare
---

# Compare software

Pairs that people often confuse. Fields come from each software page and the projects' own documentation.

## ArcGIS Pro and QGIS

| | [ArcGIS Pro](../software/desktop-gis/arcgis-pro.md) | [QGIS](../software/desktop-gis/qgis.md) |
| --- | --- | --- |
| Developer | Esri | QGIS.org community |
| License | Proprietary | GPL-2.0-or-later |
| Cost | Paid | Free |
| Platforms | Windows | Windows, macOS, Linux |
| Scripting | Python with ArcPy, .NET SDK | Python with PyQGIS, plugins |
| Extensions | Licensed separately (Spatial Analyst, Image Analyst and others) | Plugins and Processing providers such as GRASS and SAGA |

Use ArcGIS Pro inside an Esri-based organization. Use QGIS for a free, cross-platform tool with open formats.

## GeoPandas and sf

| | [GeoPandas](../software/python/geopandas.md) | [sf](../software/r/sf.md) |
| --- | --- | --- |
| Language | Python | R |
| Data model | Pandas DataFrame with geometry column | Data frame with `sfc` geometry column |
| Geometry engine | Shapely on GEOS | GEOS, with s2 for spherical operations |
| File I/O | pyogrio or Fiona on GDAL | GDAL |
| License | BSD-3-Clause | GPL-2.0 or MIT |

Both follow the OGC Simple Features model, so concepts transfer directly.

## terra, rasterio and xarray

| | [terra](../software/r/terra.md) | [rasterio](../software/python/rasterio.md) | [xarray](../software/python/xarray.md) |
| --- | --- | --- | --- |
| Language | R | Python | Python |
| Model | SpatRaster layers | NumPy arrays with a transform | Labeled N-dimensional arrays |
| Best for | Raster and vector work in one package | Reading, writing and warping rasters | NetCDF, Zarr and time series |
| Spatial extras | Built in | Use with rioxarray for labeled arrays | [rioxarray](../software/python/rioxarray.md) adds CRS and reprojection |

## Leaflet, OpenLayers and MapLibre GL JS

| | [Leaflet](../software/web-mapping/leaflet.md) | [OpenLayers](../software/web-mapping/openlayers.md) | [MapLibre GL JS](../software/web-mapping/maplibre-gl-js.md) |
| --- | --- | --- | --- |
| Rendering | DOM and canvas | Canvas and WebGL | WebGL |
| Tiles | Raster by default, vector through plugins | Raster and vector | Vector, with raster support |
| Projections | Web Mercator focus | Many projections | Web Mercator and globe |
| License | BSD-2-Clause | BSD-2-Clause | BSD-3-Clause |
| Fit | Simple maps, small size | OGC services, custom projections | Styled vector maps, 3D terrain |

## GeoServer, MapServer and QGIS Server

| | [GeoServer](../software/servers-tiles/geoserver.md) | [MapServer](../software/servers-tiles/mapserver.md) | [QGIS Server](../software/servers-tiles/qgis-server.md) |
| --- | --- | --- | --- |
| Language | Java | C | C++ with Python plugins |
| Configuration | Web admin UI and REST API | Mapfile text configuration | QGIS project files |
| License | GPL-2.0 | MIT | GPL-2.0-or-later |
| Fit | Many users and layers, admin UI | Lightweight, high performance | Reuse desktop styling online |

## PostGIS, SpatiaLite and DuckDB spatial

| | [PostGIS](../software/databases/postgis.md) | [SpatiaLite](../software/core-libraries/spatialite.md) | [DuckDB spatial](../software/databases/duckdb-spatial.md) |
| --- | --- | --- | --- |
| Model | Client-server database | Single-file embedded database | In-process analytical engine |
| Concurrency | Many writers | Single writer | Analytical, single process |
| Best for | Shared, transactional data | Portable files, mobile | Fast queries on files and Parquet |
| License | GPL-2.0-or-later | MPL, GPL or LGPL | MIT |

## Mapbox GL JS and MapLibre GL JS

| | [Mapbox GL JS](../software/web-mapping/mapbox-gl-js.md) | [MapLibre GL JS](../software/web-mapping/maplibre-gl-js.md) |
| --- | --- | --- |
| License | Proprietary from v2.0 | BSD-3-Clause |
| Access token | Required | Not required by the library |
| Origin | Mapbox | Fork of Mapbox GL JS v1.13 |
| Data | Mapbox services by default | Any vector tile source |

## OSRM, Valhalla and GraphHopper

| | [OSRM](../software/geocoding-routing/osrm.md) | [Valhalla](../software/geocoding-routing/valhalla.md) | [GraphHopper](../software/geocoding-routing/graphhopper.md) |
| --- | --- | --- | --- |
| Language | C++ | C++ | Java |
| License | BSD-2-Clause | MIT | Apache-2.0 |
| Data | OpenStreetMap | OpenStreetMap | OpenStreetMap |
| Features | Fast car, bike and foot routing, matrix, map matching | Dynamic costing, isochrones, multimodal | Custom routing models, optimization API |
