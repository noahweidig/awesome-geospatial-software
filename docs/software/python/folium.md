---
title: "folium"
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
  - Web mapping
  - Visualization
---

# ![](../../assets/logos/folium.png){ .title-logo } folium

Builds Leaflet maps from Python with choropleths, markers and plugins and exports them to standalone HTML.

[:lucide-download: Get the software](https://python-visualization.github.io/folium/latest/getting_started.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://python-visualization.github.io/folium/){ .md-button }
[:lucide-code: Source code](https://github.com/python-visualization/folium){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | folium contributors |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import folium
    m = folium.Map(location=[37.77, -122.42], zoom_start=11)
    folium.Marker([37.77, -122.42], tooltip="SF").add_to(m)
    m.save("map.html")
    ```


## Related software

- [Leaflet](../web-mapping/leaflet.md)
- [ipyleaflet](../python/ipyleaflet.md)
- [leafmap](../python/leafmap.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "folium", "description": "Builds Leaflet maps from Python with choropleths, markers and plugins and exports them to standalone HTML.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/folium/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "folium contributors"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "Python", "Open source", "Active", "MIT", "Web mapping", "Visualization"], "license": "MIT", "sameAs": "https://python-visualization.github.io/folium/", "downloadUrl": "https://python-visualization.github.io/folium/latest/getting_started.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/folium.png", "codeRepository": "https://github.com/python-visualization/folium"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
