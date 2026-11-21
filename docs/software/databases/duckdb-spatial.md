---
title: "DuckDB spatial extension"
icon: lucide/database
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/databases.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - Command line
  - Notebook
  - C++
  - SQL
  - Open source
  - Active
  - MIT
  - Spatial database
  - Cloud-native
  - Big data
---

# ![](../../assets/logos/duckdb-spatial.png){ .title-logo } DuckDB spatial extension

DuckDB extension that adds geometry types, spatial functions and GDAL-based file reading to an in-process analytical database.

[:lucide-download: Get the software](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://duckdb.org/docs/stable/core_extensions/spatial/functions.html){ .md-button }
[:lucide-code: Source code](https://github.com/duckdb/duckdb-spatial){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | DuckDB |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | C++, SQL |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Command line, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "SQL"

    ```sql
    INSTALL spatial; LOAD spatial;
    SELECT count(*) FROM ST_Read('counties.gpkg') WHERE ST_Area(geom) > 1;
    ```


## Related software

- [PostGIS](../databases/postgis.md)
- [SpatiaLite](../core-libraries/spatialite.md)
- [GeoArrow](../core-libraries/geoarrow.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "DuckDB spatial extension", "description": "DuckDB extension that adds geometry types, spatial functions and GDAL-based file reading to an in-process analytical database.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/databases/duckdb-spatial/", "applicationCategory": "Spatial databases & big data", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["C++", "SQL"], "author": {"@type": "Organization", "name": "DuckDB"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Command line", "Notebook", "C++", "SQL", "Open source", "Active", "MIT", "Spatial database", "Cloud-native", "Big data"], "license": "MIT", "sameAs": "https://duckdb.org/docs/stable/core_extensions/spatial/functions.html", "downloadUrl": "https://duckdb.org/docs/stable/core_extensions/spatial/overview.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/duckdb-spatial.png", "codeRepository": "https://github.com/duckdb/duckdb-spatial"}</script>

[:lucide-arrow-left: Back to Spatial databases & big data](index.md){ .md-button }
