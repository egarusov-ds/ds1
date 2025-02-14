import os.path

import kagglehub

from constants.extensions import Extensions
from utils.files.base import get_filepath_from_directory
from utils.files.reader import Reader


class Dataloader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = Reader(self.filepath).data

    @classmethod
    def from_kaggle_path(cls, kaggle_path: str):
        path = kagglehub.dataset_download(kaggle_path)
        if os.path.isdir(path):
            filepath = get_filepath_from_directory(path, tuple(ext.value for ext in Extensions))
        else:
            filepath = path
        return Dataloader(filepath)


if __name__ == '__main__':
    _path = "amirmotefaker/twitter-stock-market-dataset"
    data = Dataloader.from_kaggle_path(_path).data
    print('bp')
    print('bp')
    print('bp')
