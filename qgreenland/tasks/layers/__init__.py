from qgreenland.tasks.layers.arctic_dem import ArcticDEM
from qgreenland.tasks.layers.background_image import BackgroundImage
from qgreenland.tasks.layers.bedmachine import BedMachineDataset
from qgreenland.tasks.layers.glacier_terminus import GlacierTerminus
from qgreenland.tasks.layers.rarred_shapefile import RarredShapefile
from qgreenland.tasks.layers.velocity_mosaic import VelocityMosaic
from qgreenland.tasks.layers.zipped_shapefile import ZippedShapefile

# TODO: Replace mapping with programmatic lookup. Either take exact
# strings and look it up in the available imported modules, or
# programmatically convert snake/camel case?
INGEST_TASKS = {
    'arctic_dem': ArcticDEM,
    'background_image': BackgroundImage,
    'bedmachine': BedMachineDataset,
    'glacier_terminus': GlacierTerminus,
    'rarred_shapefile': RarredShapefile,
    'velocity_mosaic': VelocityMosaic,
    'zipped_shapefile': ZippedShapefile
}
