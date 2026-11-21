---
title: "GRASS GIS"
icon: lucide/monitor
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/desktop-gis.yml
tags:
  - Windows
  - macOS
  - Linux
  - GUI
  - Command line
  - Library
  - Notebook
  - C
  - Python
  - Open source
  - Active
  - GPL
  - Raster
  - Vector
  - Terrain
  - Hydrology
  - Time series
  - OSGeo
---

# ![](../../assets/logos/grass-gis.png){ .title-logo } GRASS GIS

Open source GIS for raster, vector, imagery and time-series analysis with hundreds of modules, usable from a GUI, the command line, Python or notebooks.

[:lucide-download: Get the software](https://grass.osgeo.org/download/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://grass.osgeo.org/learn/){ .md-button }
[:lucide-code: Source code](https://github.com/OSGeo/grass){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | GRASS Development Team |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | C, Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | GUI, Command line, Library, Notebook |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | GPL-2.0-or-later |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "Python"

    ```python
    import grass.script as gs
    gs.run_command("g.region", raster="elevation")
    gs.run_command("r.slope.aspect", elevation="elevation", slope="slope")
    ```


## Related software

- [QGIS](../desktop-gis/qgis.md)
- [SAGA GIS](../desktop-gis/saga-gis.md)
- [WhiteboxTools](../terrain-hydrology/whiteboxtools.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "GRASS GIS", "description": "Open source GIS for raster, vector, imagery and time-series analysis with hundreds of modules, usable from a GUI, the command line, Python or notebooks.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/desktop-gis/grass-gis/", "applicationCategory": "Desktop GIS & map viewers", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["C", "Python"], "author": {"@type": "Organization", "name": "GRASS Development Team"}, "keywords": ["Windows", "macOS", "Linux", "GUI", "Command line", "Library", "Notebook", "C", "Python", "Open source", "Active", "GPL", "Raster", "Vector", "Terrain", "Hydrology", "Time series", "OSGeo"], "license": "GPL-2.0-or-later", "sameAs": "https://grass.osgeo.org/learn/", "downloadUrl": "https://grass.osgeo.org/download/", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/grass-gis.png", "codeRepository": "https://github.com/OSGeo/grass"}</script>

[:lucide-arrow-left: Back to Desktop GIS & map viewers](index.md){ .md-button }
