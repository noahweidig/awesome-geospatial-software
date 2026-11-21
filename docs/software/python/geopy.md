---
title: "GeoPy"
icon: lucide/file-code
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/python.yml
tags:
  - Windows
  - macOS
  - Linux
  - Library
  - Python
  - Open source
  - Active
  - MIT
  - Geocoding
  - Geodesy
---

# ![](../../assets/logos/geopy.png){ .title-logo } GeoPy

Python client for many geocoding services and geodesic distance calculations.

[:lucide-download: Get the software](https://geopy.readthedocs.io/en/stable/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://geopy.readthedocs.io/){ .md-button }
[:lucide-code: Source code](https://github.com/geopy/geopy){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | GeoPy contributors |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | Library |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | MIT |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    from geopy.geocoders import Nominatim
    loc = Nominatim(user_agent="my-app").geocode("Eiffel Tower")
    print(loc.latitude, loc.longitude)
    ```


## Related software

- [Nominatim](../geocoding-routing/nominatim.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "GeoPy", "description": "Python client for many geocoding services and geodesic distance calculations.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/python/geopy/", "applicationCategory": "Python libraries", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["Python"], "author": {"@type": "Organization", "name": "GeoPy contributors"}, "keywords": ["Windows", "macOS", "Linux", "Library", "Python", "Open source", "Active", "MIT", "Geocoding", "Geodesy"], "license": "MIT", "sameAs": "https://geopy.readthedocs.io/", "downloadUrl": "https://geopy.readthedocs.io/en/stable/", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/geopy.png", "codeRepository": "https://github.com/geopy/geopy"}</script>

[:lucide-arrow-left: Back to Python libraries](index.md){ .md-button }
