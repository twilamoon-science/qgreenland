"""common.py: Tasks that could apply to any type of dataproduct."""
import os
import re
import zipfile

import luigi
import rarfile
from osgeo import gdal

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir


class Decompress(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/decompress/')


class Unrar(Decompress):
    def run(self):
        rar_path = find_single_file_by_ext(self.input().path, ext='.rar')
        rar = rarfile.RarFile(rar_path)

        with temporary_path_dir(self.output()) as temp_path:
            rar.extractall(path=temp_path)


class Unzip(Decompress):
    def run(self):
        default_filename_pattern = '.*'
        unzip_kwargs = self.layer_cfg.get('unzip_kwargs', {})
        pattern = unzip_kwargs.get('filename_pattern', default_filename_pattern)
        regex = re.compile(pattern)

        zf_path = find_single_file_by_ext(self.input().path, ext='.zip')
        zf = zipfile.ZipFile(zf_path)

        with temporary_path_dir(self.output()) as temp_path:
            for fn in zf.namelist():
                if regex.match(fn):
                    zf.extract(fn, temp_path)
            zf.close()


class ExtractNcDataset(LayerTask):
    """Extracts dataset `dataset_name` from input .nc file."""

    task_type = TaskType.WIP
    dataset_name = luigi.Parameter()

    def output(self):
        # GDAL translate will automatically determine file type from the extension.
        return luigi.LocalTarget(
            os.path.join(self.outdir, 'extract')
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_dir:
            input_fp = find_single_file_by_ext(self.input().path, ext='.nc')

            output_filename = f"{self.dataset_name}{self.layer_cfg['file_type']}"
            output_fp = os.path.join(temp_dir, output_filename)

            gdal.Translate(
                output_fp,
                f'NETCDF:{input_fp}:{self.dataset_name}'
            )
