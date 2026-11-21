---
title: "Turf.js"
icon: lucide/globe
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/web-mapping.yml
tags:
  - Web browser
  - Linux
  - macOS
  - Windows
  - Library
  - JavaScript
  - TypeScript
  - Open source
  - Active
  - MIT
  - Vector
  - Geoprocessing
---

# ![](../../assets/logos/turf-js.png){ .title-logo } Turf.js

Modular JavaScript library for geospatial analysis in the browser or Node.js, with buffers, joins, interpolation and measurement.

[:lucide-download: Get the software](https://turfjs.org/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://turfjs.org/){ .md-button }
[:lucide-code: Source code](https://github.com/Turfjs/turf){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Turf contributors |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Web browser, Linux, macOS, Windows |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | JavaScript, TypeScript |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "JavaScript"

    ```javascript
    import * as turf from "@turf/turf";
    const buffered = turf.buffer(turf.point([-75.34, 39.98]), 500, { units: "meters" });
    ```


## Related software

- [turf-swift](../other-languages/turf-swift.md)
- [JSTS](../web-mapping/jsts.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "Turf.js", "description": "Modular JavaScript library for geospatial analysis in the browser or Node.js, with buffers, joins, interpolation and measurement.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/web-mapping/turf-js/", "applicationCategory": "Web mapping libraries & SDKs", "operatingSystem": "Web browser, Linux, macOS, Windows", "programmingLanguage": ["JavaScript", "TypeScript"], "author": {"@type": "Organization", "name": "Turf contributors"}, "keywords": ["Web browser", "Linux", "macOS", "Windows", "Library", "JavaScript", "TypeScript", "Open source", "Active", "MIT", "Vector", "Geoprocessing"], "license": "MIT", "sameAs": "https://turfjs.org/", "downloadUrl": "https://turfjs.org/", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/turf-js.png", "codeRepository": "https://github.com/Turfjs/turf"}</script>

[:lucide-arrow-left: Back to Web mapping libraries & SDKs](index.md){ .md-button }
