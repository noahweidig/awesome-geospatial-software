---
title: "QGIS"
icon: lucide/monitor
edit_url: https://github.com/noahweidig/awesome-geospatial-software/edit/main/data/software/desktop-gis.yml
tags:
  - Windows
  - macOS
  - Linux
  - GUI
  - Command line
  - Plugin
  - C++
  - Python
  - Open source
  - Active
  - GPL
  - Vector
  - Raster
  - Cartography
  - Geoprocessing
  - 3D
  - OSGeo
---

# ![](../../assets/logos/qgis.png){ .title-logo } QGIS

Free, open source desktop GIS for viewing, editing, analyzing and publishing spatial data, extensible with Python plugins and the Processing framework.

[:lucide-download: Get the software](https://qgis.org/download/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://docs.qgis.org/){ .md-button }
[:lucide-code: Source code](https://github.com/qgis/QGIS){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who develops or maintains the software" } Developer | QGIS.org |
| :lucide-monitor-smartphone:{ title="Operating systems and delivery" } Platforms | Windows, macOS, Linux |
| :lucide-code-xml:{ title="Implementation or scripting languages" } Languages | C++, Python |
| :lucide-mouse-pointer-click:{ title="How you use it" } Interface | GUI, Command line, Plugin |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | GPL-2.0-or-later |
| :lucide-circle-dollar-sign:{ title="What it costs to use" } Cost | Open source |
| :lucide-activity:{ title="Development state when the entry was written" } Status | Active |

## Quick start

=== "PyQGIS"

    ```python
    from qgis.core import QgsVectorLayer, QgsProject
    layer = QgsVectorLayer("roads.gpkg|layername=roads", "roads", "ogr")
    QgsProject.instance().addMapLayer(layer)
    print(layer.featureCount())
    ```


## Related software

- [GRASS GIS](../desktop-gis/grass-gis.md)
- [SAGA GIS](../desktop-gis/saga-gis.md)
- [ArcGIS Pro](../desktop-gis/arcgis-pro.md)
- [QGIS Server](../servers-tiles/qgis-server.md)
- [QField](../field-mobile/qfield.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "SoftwareApplication", "name": "QGIS", "description": "Free, open source desktop GIS for viewing, editing, analyzing and publishing spatial data, extensible with Python plugins and the Processing framework.", "url": "https://noahweidig.github.io/awesome-geospatial-software/software/desktop-gis/qgis/", "applicationCategory": "Desktop GIS & map viewers", "operatingSystem": "Windows, macOS, Linux", "programmingLanguage": ["C++", "Python"], "author": {"@type": "Organization", "name": "QGIS.org"}, "keywords": ["Windows", "macOS", "Linux", "GUI", "Command line", "Plugin", "C++", "Python", "Open source", "Active", "GPL", "Vector", "Raster", "Cartography", "Geoprocessing", "3D", "OSGeo"], "license": "GPL-2.0-or-later", "sameAs": "https://docs.qgis.org/", "downloadUrl": "https://qgis.org/download/", "image": "https://noahweidig.github.io/awesome-geospatial-software/assets/logos/qgis.png", "codeRepository": "https://github.com/qgis/QGIS"}</script>

[:lucide-arrow-left: Back to Desktop GIS & map viewers](index.md){ .md-button }
