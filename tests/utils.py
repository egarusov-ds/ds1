import os

from constants.paths import Paths


def get_test_filepath(ext: str) -> str:
    return os.path.join(Paths.DIR_TEST_DATA, f'test.{ext}')
