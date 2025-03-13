import os

import kagglehub

from auxiliary.files.base import get_filepath_from_directory
from auxiliary.files.reader import Reader
from constants.base import Extensions


class DataLoader:
    """A simple wrapper around pandas Dataframe"""

    def __init__(self, filepath: str, **read_kwargs):
        self.filepath = filepath
        self.data = Reader(self.filepath, **read_kwargs).data

    @classmethod
    def from_kaggle_path(cls, kaggle_path: str, **read_kwargs):
        path = kagglehub.dataset_download(kaggle_path)
        if os.path.isdir(path):
            filepath = get_filepath_from_directory(path, tuple(ext.value for ext in Extensions))
        else:
            filepath = path
        return DataLoader(filepath, **read_kwargs)

    def __getattr__(self, item):
        return getattr(self.data, item)

    def __repr__(self):
        return f'{type(self).__name__}({self.filepath})'
