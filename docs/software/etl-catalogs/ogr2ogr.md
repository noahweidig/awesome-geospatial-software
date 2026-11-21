---
title: "ogr2ogr"
icon: lucide/arrow-left-right
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/etl-catalogs.yml
tags:
  - Windows
  - macOS
  - Linux
  - Command line
  - C++
  - Open source
  - Active
  - MIT
  - ETL
  - Vector
  - GDAL-based
  - OSGeo
---

# ![](../../assets/logos/ogr2ogr.png){ .title-logo } ogr2ogr

GDAL command line program that converts vector data between formats, reprojects, filters with SQL and loads data into databases.

[:lucide-download: Get the software](https://gdal.org/en/stable/programs/ogr2ogr.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://gdal.org/en/stable/programs/ogr2ogr.html){ .md-button }
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
    ogr2ogr -f GPKG parcels.gpkg parcels.shp -t_srs EPSG:4326
    ogr2ogr -f PostgreSQL PG:"dbname=gis" parcels.gpkg -nln parcels
    ogr2ogr -f Parquet parcels.parquet parcels.gpkg
    ```


## Related software

- [GDAL](../core-libraries/gdal.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "ogr2ogr", "description": "GDAL command line program that converts vector data between formats, reprojects, filters with SQL and loads data into databases.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/etl-catalogs/ogr2ogr/", "applicationCategory": "Data conversion, ETL & catalogs", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["C++"], "author": {"@type": "Organization", "name": "OSGeo"}, "keywords": ["Windows", "macOS", "Linux", "Command line", "C++", "Open source", "Active", "MIT", "ETL", "Vector", "GDAL-based", "OSGeo"], "license": "MIT", "sameAs": "https://gdal.org/en/stable/programs/ogr2ogr.html", "downloadUrl": "https://gdal.org/en/stable/programs/ogr2ogr.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/ogr2ogr.png", "codeRepository": "https://github.com/OSGeo/gdal"}</script>

[:lucide-arrow-left: Back to Data conversion, ETL & catalogs](index.md){ .md-button }
