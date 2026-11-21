---
title: "tippecanoe"
icon: lucide/server
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/servers-tiles.yml
tags:
  - macOS
  - Linux
  - Command line
  - C++
  - Open source
  - Active
  - BSD
  - Vector tiles
  - Tiles
---

# tippecanoe

Builds vector tilesets from large GeoJSON, FlatGeobuf and CSV collections, choosing which features to drop or simplify at each zoom level.

[:lucide-download: Get the software](https://github.com/felt/tippecanoe){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://github.com/felt/tippecanoe#readme){ .md-button }
[:lucide-code: Source code](https://github.com/felt/tippecanoe){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Felt |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | C++ |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | BSD-2-Clause |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Command line"

    ```bash
    tippecanoe -zg -o out.pmtiles --drop-densest-as-needed in.geojson
    ```


## Related software

- [PMTiles](../servers-tiles/pmtiles.md)
- [Planetiler](../servers-tiles/planetiler.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "tippecanoe", "description": "Builds vector tilesets from large GeoJSON, FlatGeobuf and CSV collections, choosing which features to drop or simplify at each zoom level.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/servers-tiles/tippecanoe/", "applicationCategory": "Map servers, tiles & APIs", "operatingSystem": "macOS, Linux", "programmingLanguage": ["C++"], "author": {"@type": "Organization", "name": "Felt"}, "keywords": ["macOS", "Linux", "Command line", "C++", "Open source", "Active", "BSD", "Vector tiles", "Tiles"], "license": "BSD-2-Clause", "sameAs": "https://github.com/felt/tippecanoe#readme", "downloadUrl": "https://github.com/felt/tippecanoe", "codeRepository": "https://github.com/felt/tippecanoe"}</script>

[:lucide-arrow-left: Back to Map servers, tiles & APIs](index.md){ .md-button }
