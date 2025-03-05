from typing import SupportsFloat

import pandas as pd

from constants.base import FillMethods


def get_missing_counts(df: pd.DataFrame) -> dict[str, int]:
    return {col: get_missing_count(df, col) for col in df.columns}


def get_missing_count(df: pd.DataFrame, column: str) -> int:
    return df[column].isnull().sum()


def print_missing_counts(df: pd.DataFrame) -> None:
    for col, missing_count in get_missing_counts(df).items():
        print(f'Number of missing values in "{col}" column: {missing_count}.')


def fill_missing_values(df: pd.DataFrame, column: str, method: FillMethods) -> None:
    df[column] = df[column].fillna(get_value_to_fill(df, column, method))


def get_value_to_fill(df: pd.DataFrame, column: str, method: FillMethods) -> SupportsFloat:
    values = df[column]
    try:
        value_getter = {
            FillMethods.MEDIAN: pd.Series.median,
            FillMethods.MEAN: pd.Series.mean,
            FillMethods.MOST_FREQUENT: lambda vals: vals.value_counts().argmax(),
        }[method]
        return value_getter(values)
    except KeyError:
        raise KeyError(f'Method "{method}" not supported')

def get_downsampled(df: pd.DataFrame, target: str) -> pd.DataFrame:
    cnt = collections.Counter(dataframe['y'])
    print(f'Statistics on target variable: {cnt}')
    # looks highly imbalanced, let's downsample it
    new_max_count = min(cnt.values())