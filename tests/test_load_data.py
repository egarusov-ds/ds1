import pandas as pd
import pytest

from constants.base import Extensions, KaggleDatasetPaths
from tests.utils import get_test_filepath
from utils.ds import DataLoader
from utils.files import Reader

_MAP_EXT_KAGGLE_DS = {
    Extensions.CSV: KaggleDatasetPaths.TWITTER_STOCK,
    Extensions.XLSX: KaggleDatasetPaths.YAHOO_FINANCE,
    Extensions.JSON: KaggleDatasetPaths.IRIS,
}


@pytest.mark.parametrize('ext', Extensions)
class TestLoadData:
    @staticmethod
    def _check_data(data):
        assert isinstance(data, pd.DataFrame)

    def test_reader_init(self, ext: Extensions):
        self._check_data(Reader(get_test_filepath(ext.value)).data)

    def test_dataloader_init(self, ext: Extensions):
        self._check_data(DataLoader(get_test_filepath(ext.value)).data)

    def test_dataloader_from_kaggle_path(self, ext: Extensions):
        kaggle_path = _MAP_EXT_KAGGLE_DS[ext]
        self._check_data(DataLoader.from_kaggle_path(kaggle_path).data)
