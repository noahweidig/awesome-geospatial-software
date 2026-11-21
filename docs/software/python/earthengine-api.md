---
title: "Earth Engine Python API"
icon: lucide/file-code
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/python.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - Notebook
  - API
  - Python
  - Free to use
  - Active
  - Apache-2.0
  - Earth observation
  - Cloud-native
  - Google
---

# ![](../../assets/logos/earthengine-api.png){ .title-logo } Earth Engine Python API

Python client library for Google Earth Engine that runs analyses server side on its data catalog.

[:lucide-download: Get the software](https://developers.google.com/earth-engine/guides/python_install){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://developers.google.com/earth-engine/guides){ .md-button }
[:lucide-code: Source code](https://github.com/google/earthengine-api){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | Google |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library, Notebook, API |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Apache-2.0 |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Free to use |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

!!! warning "Caveat"

    The client library is open source. Using Earth Engine requires a registered Google Cloud project, and commercial use needs a paid plan.

## Quick start

=== "Python"

    ```python
    import ee
    ee.Authenticate(); ee.Initialize(project="my-project")
    img = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED").filterDate("2025-06-01", "2025-06-30").median()
    ```


## Related software

- [Google Earth Engine](../remote-sensing/google-earth-engine.md)
- [geemap](../python/geemap.md)
- [rgee](../r/rgee.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "Earth Engine Python API", "description": "Python client library for Google Earth Engine that runs analyses server side on its data catalog.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/earthengine-api/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "Google"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Notebook", "API", "Python", "Free to use", "Active", "Apache-2.0", "Earth observation", "Cloud-native", "Google"], "license": "Apache-2.0", "sameAs": "https://developers.google.com/earth-engine/guides", "downloadUrl": "https://developers.google.com/earth-engine/guides/python_install", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/earthengine-api.png", "codeRepository": "https://github.com/google/earthengine-api"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
