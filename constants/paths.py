from os.path import dirname, abspath, join as path_join


class Paths:
    DIR_MAIN = dirname(dirname(abspath(__file__)))
    DIR_DATA = path_join(DIR_MAIN, 'data')
    DIR_TEST_DATA = path_join(DIR_DATA, 'test')
