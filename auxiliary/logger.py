import logging
import os
from typing import Optional


class Logger:
    _instance: object = None
    _logger: logging.Logger
    _stream_handler: Optional[logging.StreamHandler]
    _file_handler: Optional[logging.FileHandler]

    _format: str = "%(asctime)s [%(levelname)-5.5s] %(message)s"

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            obj = super().__new__(cls)
            obj._logger = logging.getLogger()
            obj._stream_handler = logging.StreamHandler()
            obj._file_handler = logging.FileHandler(cls.get_filename())
            obj._logger.setLevel(logging.INFO)
            for handler in (obj._stream_handler, obj._file_handler):
                handler.setFormatter(logging.Formatter(cls._format))
                obj._logger.addHandler(handler)
            cls._instance = obj
        return cls._instance

    @staticmethod
    def get_filename() -> str:
        return os.path.join(os.getcwd(), 'log.txt')

    def log(self, msg: str, level=logging.INFO) -> None:
        self._logger.log(level, msg)


def log(msg: str, level=logging.INFO) -> None:
    Logger().log(msg, level=level)
