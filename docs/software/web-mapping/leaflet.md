---
title: "Leaflet"
icon: lucide/globe
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/web-mapping.yml
tags:
  - Web browser
  - Library
  - JavaScript
  - Open source
  - Active
  - BSD
  - Web mapping
  - Raster tiles
---

# ![](../../assets/logos/leaflet.png){ .title-logo } Leaflet

Small, mobile-friendly JavaScript library for interactive maps, with a large plugin ecosystem.

[:lucide-download: Get the software](https://leafletjs.com/download.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://leafletjs.com/reference.html){ .md-button }
[:lucide-code: Source code](https://github.com/Leaflet/Leaflet){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Leaflet contributors |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Web browser |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | JavaScript |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | BSD-2-Clause |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "JavaScript"

    ```javascript
    const map = L.map("map").setView([51.505, -0.09], 13);
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "&copy; OpenStreetMap contributors"
    }).addTo(map);
    ```


## Related software

- [OpenLayers](../web-mapping/openlayers.md)
- [MapLibre GL JS](../web-mapping/maplibre-gl-js.md)
- [folium](../python/folium.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "Leaflet", "description": "Small, mobile-friendly JavaScript library for interactive maps, with a large plugin ecosystem.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/web-mapping/leaflet/", "applicationCategory": "Web mapping libraries & SDKs", "operatingSystem": "Web browser", "programmingLanguage": ["JavaScript"], "author": {"@type": "Organization", "name": "Leaflet contributors"}, "keywords": ["Web browser", "Library", "JavaScript", "Open source", "Active", "BSD", "Web mapping", "Raster tiles"], "license": "BSD-2-Clause", "sameAs": "https://leafletjs.com/reference.html", "downloadUrl": "https://leafletjs.com/download.html", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/leaflet.png", "codeRepository": "https://github.com/Leaflet/Leaflet"}</script>

[:lucide-arrow-left: Back to Web mapping libraries & SDKs](index.md){ .md-button }
