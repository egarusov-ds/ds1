import os.path
from typing import SupportsFloat

import kagglehub
import pandas

from constants.base import Extensions, FillMethods
from utils.files.base import get_filepath_from_directory
from utils.files.reader import Reader


class Dataloader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        print(f"{self}: reading data.")
        self.data = Reader(self.filepath).data

    @classmethod
    def from_kaggle_path(cls, kaggle_path: str):
        path = kagglehub.dataset_download(kaggle_path)
        if os.path.isdir(path):
            filepath = get_filepath_from_directory(path, tuple(ext.value for ext in Extensions))
        else:
            filepath = path
        return Dataloader(filepath)

    def __getattr__(self, item):
        return getattr(self.data, item)

    def get_missing_counts(self) -> dict[str, int]:
        return {col: self.get_missing_count(col) for col in self.columns}

    def get_missing_count(self, column: str) -> int:
        return self.data[column].isnull().sum()

    def print_missing_counts(self) -> None:
        for col, missing_count in self.get_missing_counts().items():
            print(f'Number of missing values in "{col}" column: {missing_count}.')

    def fill_missing(self, column: str, method: FillMethods) -> None:
        self.data[column] = self.data[column].fillna(self.get_value_to_fill(column, method))

    def get_value_to_fill(self, column: str, method: FillMethods) -> SupportsFloat:
        values = self.data[column]
        try:
            value_getter = {
                FillMethods.MEDIAN: pandas.Series.median,
                FillMethods.MEAN: pandas.Series.mean,
                FillMethods.MOST_FREQUENT: lambda vals: vals.value_counts().argmax(),
            }[method]
            return value_getter(values)
        except KeyError:
            raise KeyError(f'Method "{method}" not supported')

    def __repr__(self):
        return f'{type(self).__name__}({self.filepath})'
