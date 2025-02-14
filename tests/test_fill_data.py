import numpy as np
import pytest

from utils.files.dataloader import Dataloader


@pytest.fixture
def dataloader():
    return Dataloader.from_kaggle_path("sachinkumar62/datascience-job-data")


class TestFillData:
    @pytest.mark.parametrize('method', (
            'median',
            'mean',
            'most_frequent',
    ))
    def test_fill_missing(self, dataloader, method: str):
        col_name = 'training_hours'
        indices_for_missing = dataloader.data[col_name].apply(np.isnan)
        value_to_fill = dataloader.get_value_to_fill(col_name, method)
        dataloader.fill_missing(col_name, method)
        final_values = dataloader.data[col_name][indices_for_missing].to_numpy()
        assert set(final_values) == {value_to_fill}
