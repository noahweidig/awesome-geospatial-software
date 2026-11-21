---
title: "Osmium Tool"
icon: lucide/map-pinned
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/osm.yml
tags:
  - Linux
  - macOS
  - Windows
  - Command line
  - C++
  - Open source
  - Active
  - GPL
  - OpenStreetMap
  - ETL
---

# Osmium Tool

Command line tool for filtering, extracting, merging and converting OpenStreetMap data files, built on libosmium.

[:lucide-download: Get the software](https://osmcode.org/osmium-tool/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://docs.osmcode.org/osmium/latest/){ .md-button }
[:lucide-code: Source code](https://github.com/osmcode/osmium-tool){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Jochen Topf |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Linux, macOS, Windows |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | C++ |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Command line |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | GPL-3.0 |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Command line"

    ```bash
    osmium extract -b -122.6,37.6,-122.3,37.9 planet.osm.pbf -o sf.osm.pbf
    osmium tags-filter sf.osm.pbf w/highway -o roads.osm.pbf
    ```


## Related software

- [osm2pgsql](../osm/osm2pgsql.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "Osmium Tool", "description": "Command line tool for filtering, extracting, merging and converting OpenStreetMap data files, built on libosmium.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/osm/osmium-tool/", "applicationCategory": "OpenStreetMap tools", "operatingSystem": "Linux, macOS, Windows", "programmingLanguage": ["C++"], "author": {"@type": "Organization", "name": "Jochen Topf"}, "keywords": ["Linux", "macOS", "Windows", "Command line", "C++", "Open source", "Active", "GPL", "OpenStreetMap", "ETL"], "license": "GPL-3.0", "sameAs": "https://docs.osmcode.org/osmium/latest/", "downloadUrl": "https://osmcode.org/osmium-tool/", "codeRepository": "https://github.com/osmcode/osmium-tool"}</script>

[:lucide-arrow-left: Back to OpenStreetMap tools](index.md){ .md-button }
