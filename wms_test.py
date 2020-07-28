import qgis.core as qgc

# Supply path to qgis install location

qgc.QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

qgs = qgc.QgsApplication([], False)

# Load providers
qgs.initQgis()

# url = 'http://www.glims.org/mapservice'
# url = 'url=http://www.glims.org/mapservice?SERVICE=WMS&VERSION=1.3.0&layers=GLIMS_GLACIERS&styles=&format=image/png'

url = 'IgnoreGetMapUrl=1&contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&format=image/png&layers=GLIMS_GLACIERS&styles&tileMatrixSet=GLIMS_GLACIERS-wmsc-0&url=http://www.glims.org/mapservice?VERSION=1.3.0'

layer = qgc.QgsRasterLayer(url, 'GLIMS_GLACIERS', 'wms')

# breakpoint()

project = qgc.QgsProject.instance()
project.write('/tmp/wms_invalid.qgs')
project.addMapLayer(layer)

project.write()

print(layer)
