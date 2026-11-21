---
icon: lucide/map
---

# Geospatial primer

The concepts that decide which tool fits.

## Vector and raster

**Vector** data stores points, lines and polygons with attributes. Parcels, roads and boundaries are vectors. **Raster** data stores a grid of cells with values. Elevation, imagery and land cover are rasters. Tools usually specialize: [GeoPandas](../software/python/geopandas.md) and [sf](../software/r/sf.md) lead on vectors, [rasterio](../software/python/rasterio.md) and [terra](../software/r/terra.md) on rasters.

## Coordinate reference systems

A CRS defines how coordinates map to the Earth. EPSG:4326 (WGS 84) stores longitude and latitude in degrees. Projected systems such as UTM store meters, which you need for distance and area. [PROJ](../software/core-libraries/proj.md) does the transformations in nearly every tool on this site. Mixing CRSs without reprojecting is the most common cause of misaligned layers.

## Formats

Formats trade simplicity against scale. Shapefile is universal but old. GeoPackage is a single SQLite file. GeoParquet and FlatGeobuf suit cloud storage. See [Data formats](data-formats.md).

## Services and tiles

Servers publish data over the network. OGC services such as WMS, WFS and WMTS are the long-standing standard. OGC API Features and STAC are newer, JSON-based. Tiles pre-cut maps into small pieces for fast display: raster tiles as images, vector tiles as compact geometry. See [Map servers, tiles and APIs](../software/servers-tiles/index.md).

## Cloud-native data

Cloud Optimized GeoTIFF, GeoParquet, Zarr and PMTiles let a client read only the bytes it needs through HTTP range requests. This removes the need to download whole files or run a server. [STAC](../software/python/pystac.md) catalogs describe such assets.

## Desktop, library or service

- **Desktop GIS** suits exploration, editing and cartography.
- **Libraries** suit repeatable analysis in Python, R or Julia.
- **Servers and databases** suit sharing data with many users.
- **Cloud platforms** suit imagery archives too large to download.
