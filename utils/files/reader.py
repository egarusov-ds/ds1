import pandas

from constants.extensions import Extensions
from utils.files.base import get_extension


class Reader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = self.get_data(filepath)

    @staticmethod
    def get_data(filepath: str) -> pandas.DataFrame:
        ext = get_extension(filepath)
        try:
            reader_meth = {
                Extensions.CSV: pandas.read_csv,
                Extensions.XLSX: pandas.read_excel,
            }[Extensions(ext)]
            return reader_meth(filepath)
        except KeyError as exc:
            raise type(exc)("Format not supported: {}")
