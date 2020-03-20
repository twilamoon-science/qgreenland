from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.shapefile import KmlToShp, ReprojectShapefile
from qgreenland.util.luigi import LayerPipeline


class Minerals(LayerPipeline):
    """Rename files to their final location."""

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id'],
            override_fetch_filename=f"{self.cfg['id']}.kml"
        )  # ->
        unrar = KmlToShp(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return ReprojectShapefile(
            requires_task=unrar,
            layer_id=self.layer_id
        )
