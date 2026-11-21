---
title: "OSMnx"
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
  - MIT
  - OpenStreetMap
  - Network analysis
  - Routing
  - Urban
---

# OSMnx

Downloads OpenStreetMap street networks and other features, models them as NetworkX graphs and computes routes and network metrics.

[:lucide-download: Get the software](https://osmnx.readthedocs.io/en/stable/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://osmnx.readthedocs.io/){ .md-button }
[:lucide-code: Source code](https://github.com/gboeing/osmnx){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Geoff Boeing |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import osmnx as ox
    G = ox.graph_from_place("Piedmont, California, USA", network_type="drive")
    ox.plot_graph(G)
    ```


## Cite

Boeing, G. (2017). OSMnx. Computers, Environment and Urban Systems, 65, 126-139.

DOI: [10.1016/j.compenvurbsys.2017.05.004](https://doi.org/10.1016/j.compenvurbsys.2017.05.004)

## Related software

- [momepy](../python/momepy.md)
- [Pandana](../python/pandana.md)
- [osm2pgsql](../osm/osm2pgsql.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "OSMnx", "description": "Downloads OpenStreetMap street networks and other features, models them as NetworkX graphs and computes routes and network metrics.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/osmnx/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "Geoff Boeing"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "Python", "Open source", "Active", "MIT", "OpenStreetMap", "Network analysis", "Routing", "Urban"], "license": "MIT", "sameAs": "https://osmnx.readthedocs.io/", "downloadUrl": "https://osmnx.readthedocs.io/en/stable/", "codeRepository": "https://github.com/gboeing/osmnx", "identifier": "https://doi.org/10.1016/j.compenvurbsys.2017.05.004"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
