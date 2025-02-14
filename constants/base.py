from enum import Enum


class Extensions(Enum):
    CSV = 'csv'
    XLSX = 'xlsx'
    JSON = 'json'


class FillMethods(Enum):
    MEAN = 'mean'
    MEDIAN = 'median'
    MOST_FREQUENT = 'most_frequent'


class KaggleDatasetPaths:
    TWITTER_STOCK = "amirmotefaker/twitter-stock-market-dataset"
    YAHOO_FINANCE = "suruchiarora/yahoo-finance-dataset-2018-2023"
    IRIS = "rtatman/iris-dataset-json-version"
    DATA_SCIENCE_JOBS = "sachinkumar62/datascience-job-data"
