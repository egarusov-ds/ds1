from typing import Optional

import pandas as pd
import seaborn as sns


def get_pair_plot(df: pd.DataFrame, columns: Optional[tuple] = None, hue: Optional[str] = None, **kwargs) -> None:
    sns.pairplot(data=df, vars=columns, hue=hue, **kwargs)


def get_scatter_plot(df: pd.DataFrame, x: str, y: str, hue: Optional[str] = None, **kwargs) -> None:
    sns.scatterplot(data=df, x=x, y=y, hue=hue, **kwargs)


def get_histogram(df: pd.DataFrame, x: str, hue: Optional[str] = None, **kwargs) -> None:
    sns.histplot(data=df, x=x, hue=hue, **kwargs)


def get_linear_plot(df: pd.DataFrame, x: str, hue: Optional[str] = None, **kwargs) -> None:
    sns.lineplot(data=df, x=x, hue=hue, **kwargs)
