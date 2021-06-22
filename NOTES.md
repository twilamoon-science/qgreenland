# Notes for improvement of QGreenland

## Logistics

* meetings: 8 h diff, so proposed time is 5pm IT=7am US

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
* the plugin can also add some specific tools to make life easier to user
* it will also provide the essential documentation, plus a link to the full docs

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
