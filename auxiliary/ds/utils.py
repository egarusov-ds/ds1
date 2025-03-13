import pandas as pd

from auxiliary.logger import log


def get_most_correlated_variables(source: pd.DataFrame, target: pd.Series) -> list:
    _to_take = 10
    cols_and_correlations = [(col_name, source[col_name].corr(target)) for col_name in source.columns]
    cols_and_correlations.sort(key=lambda t: abs(t[1]), reverse=True)
    log(f"{_to_take} variables most correlated with target variable are:")
    for col_name, corr in cols_and_correlations[:_to_take]:
        log(f"  {col_name}: {corr}")
    return cols_and_correlations


def get_variable_combinations(variables: tuple) -> tuple:
    return tuple(
        (v1, v2) for i1, v1 in enumerate(variables) for v2 in variables[i1:]
        if v1 == v2 or _get_ohe_original(v1) != _get_ohe_original(v2)
    )


def _get_ohe_original(variable: str) -> str:
    res, *_ = variable.split('_')
    return res
