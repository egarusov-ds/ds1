from constants.base import KaggleDatasetPaths
from utils.db.base import DBConnection
from utils.ds.data_loader import DataLoader
from homeworks.hw3.config import DB_NAME

dataframe = DataLoader.from_kaggle_path(KaggleDatasetPaths.STARTUPS_GROWTH).data
with DBConnection.from_secrets(database=DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    # cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print('bp')
    print('bp')
    print('bp')
# with get_connection() as connection:
#     print('bp')
#     print('bp')
# print('bp')
