---
title: "MapLibre GL JS"
icon: lucide/globe
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/web-mapping.yml
tags:
  - Web browser
  - Library
  - TypeScript
  - JavaScript
  - Open source
  - Active
  - BSD
  - Web mapping
  - Vector tiles
  - 3D
  - MapLibre
---

# ![](../../assets/logos/maplibre-gl-js.png){ .title-logo } MapLibre GL JS

Open source WebGL library for vector tile maps, forked from Mapbox GL JS v1 before its license changed.

[:lucide-download: Get the software](https://maplibre.org/maplibre-gl-js/docs/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://maplibre.org/maplibre-gl-js/docs/){ .md-button }
[:lucide-code: Source code](https://github.com/maplibre/maplibre-gl-js){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | MapLibre |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Web browser |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | TypeScript, JavaScript |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | BSD-3-Clause |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "JavaScript"

    ```javascript
    const map = new maplibregl.Map({
      container: "map",
      style: "https://demotiles.maplibre.org/style.json",
      center: [0, 0], zoom: 2
    });
    ```


## Related software

- [Mapbox GL JS](../web-mapping/mapbox-gl-js.md)
- [MapLibre Native](../web-mapping/maplibre-native.md)
- [Leaflet](../web-mapping/leaflet.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "MapLibre GL JS", "description": "Open source WebGL library for vector tile maps, forked from Mapbox GL JS v1 before its license changed.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/web-mapping/maplibre-gl-js/", "applicationCategory": "Web mapping libraries & SDKs", "operatingSystem": "Web browser", "programmingLanguage": ["TypeScript", "JavaScript"], "author": {"@type": "Organization", "name": "MapLibre"}, "keywords": ["Web browser", "Library", "TypeScript", "JavaScript", "Open source", "Active", "BSD", "Web mapping", "Vector tiles", "3D", "MapLibre"], "license": "BSD-3-Clause", "sameAs": "https://maplibre.org/maplibre-gl-js/docs/", "downloadUrl": "https://maplibre.org/maplibre-gl-js/docs/", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/maplibre-gl-js.png", "codeRepository": "https://github.com/maplibre/maplibre-gl-js"}</script>

[:lucide-arrow-left: Back to Web mapping libraries & SDKs](index.md){ .md-button }
