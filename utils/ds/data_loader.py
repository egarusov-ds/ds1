import os

import kagglehub

from constants.base import Extensions
from utils.files.base import get_filepath_from_directory
from utils.files.reader import Reader


class DataLoader:
    """A simple wrapper around pandas Dataframe"""

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
        return DataLoader(filepath)

    def __getattr__(self, item):
        return getattr(self.data, item)

    def __repr__(self):
        return f'{type(self).__name__}({self.filepath})'
