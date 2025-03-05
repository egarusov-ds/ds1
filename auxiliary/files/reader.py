import pandas

from constants.base import Extensions
from auxiliary.files.base import get_extension


class Reader:
    def __init__(self, filepath: str, **read_kwargs):
        self.filepath = filepath
        self.read_kwargs = read_kwargs
        self.data = self.get_data(filepath)

    def get_data(self, filepath: str) -> pandas.DataFrame:
        ext = get_extension(filepath)
        try:
            reader_meth = {
                Extensions.CSV: pandas.read_csv,
                Extensions.XLSX: pandas.read_excel,
                Extensions.JSON: pandas.read_json,
            }[Extensions(ext)]
            return reader_meth(filepath, **self.read_kwargs)
        except KeyError as exc:
            raise type(exc)("Format not supported: {}")
