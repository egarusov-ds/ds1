import os.path
from typing import SupportsFloat

import kagglehub

from constants.extensions import Extensions
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

    def fill_missing(self, column: str, method: str) -> None:
        self.data[column].fillna(self.get_value_to_fill(column, method), inplace=True)

    def get_value_to_fill(self, column: str, method: str) -> SupportsFloat:
        values = self.data[column]
        match method:
            case 'median':
                res = values.median()
            case 'mean':
                res = values.mean()
            case 'most_frequent':
                res = values.value_counts().argmax()
            case _:
                raise ValueError(f'Method "{method}" not supported')
        return res

    def __repr__(self):
        return f'{type(self).__name__}({self.filepath})'
