import os

import pandas
import pytest

from constants.base import Extensions, KaggleDatasetPaths
from constants.paths import Paths
from utils.files.dataloader import Dataloader
from utils.files.reader import Reader

_MAP_EXT_KAGGLE_DS = {
    Extensions.CSV: KaggleDatasetPaths.TWITTER_STOCK,
    Extensions.XLSX: KaggleDatasetPaths.YAHOO_FINANCE,
    Extensions.JSON: KaggleDatasetPaths.IRIS,
}


@pytest.mark.parametrize('ext', Extensions)
class TestLoadData:
    @staticmethod
    def _check_data(data):
        assert isinstance(data, pandas.DataFrame)

    def test_reader_init(self, ext: Extensions):
        self._check_data(Reader(get_test_filepath(ext.value)).data)

    def test_dataloader_init(self, ext: Extensions):
        self._check_data(Dataloader(get_test_filepath(ext.value)).data)

    def test_dataloader_from_kaggle_path(self, ext: Extensions):
        kaggle_path = _MAP_EXT_KAGGLE_DS[ext]
        self._check_data(Dataloader.from_kaggle_path(kaggle_path).data)


def get_test_filepath(ext: str) -> str:
    return os.path.join(Paths.DIR_TEST_DATA, f'test.{ext}')
