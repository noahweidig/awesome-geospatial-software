---
icon: lucide/file
---

# Data formats

| Format | Type | Typical use | Read with |
| --- | --- | --- | --- |
| GeoTIFF | Raster | Elevation, imagery, land cover | rasterio, GDAL, terra |
| Cloud Optimized GeoTIFF | Raster | Cloud-hosted imagery read by range request | rio-cogeo, GDAL, geotiff.js |
| Shapefile | Vector | Legacy exchange of boundaries and points | GeoPandas, GDAL, sf |
| GeoPackage | Vector and raster | Single-file database, mobile, QGIS default | GDAL, GeoPandas, sf |
| GeoJSON | Vector | Web services, small extracts | GeoPandas, Turf.js, Leaflet |
| FlatGeobuf | Vector | Streaming from cloud storage | GDAL, flatgeobuf libraries |
| GeoParquet | Vector | Large analytical tables, cloud storage | DuckDB spatial, GeoPandas, GDAL |
| File Geodatabase | Vector and raster | Esri projects | GDAL, ArcGIS Pro |
| NetCDF | Multi-dimensional array | Climate, ocean and weather grids | xarray, CDO, Panoply |
| GRIB | Multi-dimensional array | Weather forecasts and reanalysis | cfgrib, xarray, Herbie |
| Zarr | Chunked array | Cloud-native data cubes | xarray |
| HDF5 | Multi-dimensional array | NASA products | GDAL, h5py |
| LAS and LAZ | Point cloud | LiDAR | PDAL, laspy, LAStools |
| KML | Vector | Google Earth sharing | GDAL, Google Earth Pro |
| MBTiles and PMTiles | Tile archive | Offline and static-hosted tiles | TileServer GL, PMTiles tools |
| Mapbox Vector Tile | Vector tiles | Web basemaps | MapLibre GL JS, OpenLayers |
| STAC | Catalog metadata | Searching imagery archives | pystac-client, rstac |

Check [GDAL's driver list](https://gdal.org/en/stable/drivers/index.html) for the full set of formats it reads and writes.
