from typing import Type

import pandas as pd
from sklearn.model_selection import GridSearchCV

from auxiliary.logger import log
from auxiliary.timer import TimerCM


def fit_with_grid_search(model_cls: Type, params: dict, source: pd.DataFrame, target: pd.Series) -> GridSearchCV:
    with TimerCM():
        log(f'Doing grid search with {model_cls.__name__} and params: {params}')
        grid_search = GridSearchCV(model_cls(), params)
        grid_search.fit(source, target)
        return grid_search
