from enum import Enum

DB_NAME = "kaggle_datasets"
TABLE_NAME = "startups_data"


class DatasetFields(Enum):
    NAME = "Startup Name"
    INDUSTRY = "Industry"
    ROUNDS = "Funding Rounds"
    INVESTMENT = "Investment Amount (USD)"
    VALUATION = "Valuation (USD)"
    INVESTORS_COUNT = "Number of Investors"
    COUNTRY = "Country"
    YEAR_FOUNDED = "Year Founded"
    RATE = "Growth Rate (%)"
