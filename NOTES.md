# Notes for improvement of QGreenland

## Logistics

* meetings: 8 h diff, so proposed time is 4pm IT=8am US

## Possible improvements of the project

* more predictable behaviour: let the user activate groups of layers with all contained layers with one click
* add scale dependent visibility?
* replace meteo data with grib or similar?
* reduce the number of classes in legend? e.g. seawater temperature
* avoid the "too many open files" issue
* add support for satellite imagery (e.g. Copernicus)

TBD: suggest further improvements (if any) to styling and general usability

## Option: replacing the project with a plugin

A plugin could work as follows:
* the plugin adds an entry to one of the menus (possibly "Web")
* from the entry the user will be able to download either the full data package, or if useful some subset of it
* the plugin can download the data and apply the style if any
* the plugin can also add some specific tools to make life easier to user
* it will also provide the essential documentation, plus a link to the full docs

Possible sources of inspiration and code:
* https://plugins.qgis.org/plugins/swissgeodownloader/
* https://plugins.qgis.org/plugins/planet_explorer/
* https://plugins.qgis.org/plugins/Dataforsyningen/
* https://plugins.qgis.org/plugins/qquake/
* https://plugins.qgis.org/plugins/geobretagne/
* https://plugins.qgis.org/plugins/israeli_opendata_loader/
* https://plugins.qgis.org/plugins/oam_qgis3_express/
* https://plugins.qgis.org/plugins/SaxonyCadastralParcels/
* https://plugins.qgis.org/plugins/ana_data_acquisition/
* https://plugins.qgis.org/plugins/tmsforkorea/
* https://plugins.qgis.org/plugins/pobieracz_danych_gugik/
* https://plugins.qgis.org/plugins/pdokservicesplugin/


## Option: WebGIS

* the same data and projects could be exposed through a webGIS. The use of QGIS-server will allow to show exactly the same styles as in the desktop project, no additional styling needed

## Further items

    • Discussion of the use of database tools
        ◦ Do any QGIS tools allow creation of a simpler method for adding/removing data layers?
        ◦ How do these tools function?
        ◦ Are we able to maintain data archive access rather than storing data ourselves?

    • Expert opinion on other QGIS considerations for future expansion and improvement of the QGreenland tool

This will be done after the completion of previous steps

    • Check whether changes within QGIS to support better QGreenland function are needed
