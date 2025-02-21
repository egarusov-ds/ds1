import json
import string
from typing import Optional, Union

import mysql.connector
import numpy as np

from constants.paths import Paths

MAP_FIELD_TYPES = {
    np.dtypes.ObjectDType(): "VARCHAR(255)",
    np.dtypes.Int64DType(): "INT",
    np.dtypes.Float64DType(): "FLOAT(24)",
}


class DBConnection:
    connection = None

    def __init__(
            self,
            username: str,
            password: str,
            host: str,
            database: Optional[str] = None
    ):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

    def __enter__(self):
        self.connection = mysql.connector.connect(
            username=self.username,
            password=self.password,
            host=self.host,
            database=self.database,
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def __getattr__(self, item):
        return getattr(self.connection, item)

    @classmethod
    def from_secrets(cls, secrets_path: str = Paths.FP_DB_SECRETS, **kwargs):
        with open(secrets_path) as file:
            data = json.load(file)
        return DBConnection(**{**data, **kwargs})


def get_column_db_repr(column_name: str, dtype, is_primary: bool) -> str:
    res = [get_db_field_name(column_name), MAP_FIELD_TYPES[dtype]]
    if is_primary:
        res.append('PRIMARY KEY')
    return " ".join(res)


def get_insert_row_single(entry: np.array) -> str:
    res = ", ".join(map(get_db_repr, entry))
    return f"({res})"


def get_db_repr(obj: Union[str, int, float]) -> str:
    if isinstance(obj, str):
        return f'"{obj}"'
    return str(obj)


def get_db_field_name(s: str) -> str:
    flt = filter(lambda c: c in string.ascii_lowercase + string.whitespace, s.strip().lower())
    return "".join(flt).strip().replace(' ', '_')
