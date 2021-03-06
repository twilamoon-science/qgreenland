from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import UngzipMany
from qgreenland.tasks.common.vector import Ogr2OgrVector
from qgreenland.util.luigi import LayerPipeline


class GzippedVectorParts(LayerPipeline):

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset']
        )  # ->
        unzip = UngzipMany(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return Ogr2OgrVector(
            requires_task=unzip,
            layer_id=self.layer_id
        )
