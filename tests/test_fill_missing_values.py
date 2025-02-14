import numpy as np
import pytest

from constants.base import FillMethods, KaggleDatasetPaths
from utils.ds import DataLoader, get_value_to_fill, fill_missing_values


@pytest.fixture
def dataframe():
    return DataLoader.from_kaggle_path(KaggleDatasetPaths.DATA_SCIENCE_JOBS).data


class TestFillMissing:
    @pytest.mark.parametrize('method', FillMethods)
    def test_fill_missing(self, dataframe, method: FillMethods):
        col_name = 'training_hours'
        indices_for_missing = dataframe[col_name].apply(np.isnan)
        value_to_fill = get_value_to_fill(dataframe, col_name, method)
        fill_missing_values(dataframe, col_name, method)
        final_values = dataframe[col_name][indices_for_missing].to_numpy()
        assert set(final_values) == {value_to_fill}
