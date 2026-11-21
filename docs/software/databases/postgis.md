---
title: "PostGIS"
icon: lucide/database
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/databases.yml
tags:
  - Windows
  - macOS
  - Linux
  - Server
  - Library
  - Command line
  - C
  - SQL
  - Open source
  - Active
  - GPL
  - Spatial database
  - Vector
  - Raster
  - OSGeo
---

# ![](../../assets/logos/postgis.png){ .title-logo } PostGIS

Spatial extension for PostgreSQL that adds geometry, geography and raster types, spatial indexes and hundreds of SQL functions.

[:lucide-download: Get the software](https://postgis.net/documentation/getting_started/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://postgis.net/documentation/){ .md-button }
[:lucide-code: Source code](https://github.com/postgis/postgis){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | OSGeo |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux, Server |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | C, SQL |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | GPL-2.0-or-later |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "SQL"

    ```sql
    CREATE EXTENSION postgis;
    SELECT name FROM cities c
    JOIN parks p ON ST_DWithin(c.geom::geography, p.geom::geography, 1000);
    ```


## Related software

- [SpatiaLite](../core-libraries/spatialite.md)
- [DuckDB spatial extension](../databases/duckdb-spatial.md)
- [pgRouting](../databases/pgrouting.md)
- [GEOS](../core-libraries/geos.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "PostGIS", "description": "Spatial extension for PostgreSQL that adds geometry, geography and raster types, spatial indexes and hundreds of SQL functions.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/databases/postgis/", "applicationCategory": "Spatial databases & big data", "operatingSystem": "Windows, macOS, Linux, Server", "programmingLanguage": ["C", "SQL"], "author": {"@type": "Organization", "name": "OSGeo"}, "keywords": ["Windows", "macOS", "Linux", "Server", "Library", "Command line", "C", "SQL", "Open source", "Active", "GPL", "Spatial database", "Vector", "Raster", "OSGeo"], "license": "GPL-2.0-or-later", "sameAs": "https://postgis.net/documentation/", "downloadUrl": "https://postgis.net/documentation/getting_started/", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/postgis.png", "codeRepository": "https://github.com/postgis/postgis"}</script>

[:lucide-arrow-left: Back to Spatial databases & big data](index.md){ .md-button }
