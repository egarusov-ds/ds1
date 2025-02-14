import os

import pandas
import pytest

from constants.extensions import Extensions
from constants.paths import Paths
from utils.files.dataloader import Dataloader
from utils.files.reader import Reader


class TestLoadData:
    @staticmethod
    def _check_data(data):
        assert isinstance(data, pandas.DataFrame)

    @pytest.mark.parametrize('ext', Extensions)
    def test_reader_init(self, ext):
        self._check_data(Reader(get_test_filepath(ext.value)).data)

    @pytest.mark.parametrize('ext', Extensions)
    def test_dataloader_init(self, ext):
        self._check_data(Dataloader(get_test_filepath(ext.value)).data)

    @pytest.mark.parametrize('path', (
            "amirmotefaker/twitter-stock-market-dataset",  # csv
            "suruchiarora/yahoo-finance-dataset-2018-2023",  # xlsx
            "rtatman/iris-dataset-json-version",  # json
    ))
    def test_dataloader_from_kaggle_path(self, path: str):
        self._check_data(Dataloader.from_kaggle_path(path).data)


def get_test_filepath(ext: str) -> str:
    return os.path.join(Paths.DIR_TEST_DATA, f'test.{ext}')
