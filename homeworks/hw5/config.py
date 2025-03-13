import numpy as np
from lightgbm import LGBMRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import Ridge, BayesianRidge

TARGET_VAR = 'price'
FEATURES_COUNT = 10
TEST_RATIO = 0.2

MAP_GRID_SEARCH_PARAMS = {
    Ridge: {
        'alpha': np.linspace(0.5, 1.5, 3),
    },
    BayesianRidge: {
        'alpha_1': np.linspace(5 * 10 ** -7, 15 * 10 ** -7, 3),
        'alpha_2': np.linspace(5 * 10 ** -7, 15 * 10 ** -7, 3),
    },
    GradientBoostingRegressor: {
        'n_estimators': np.linspace(75, 125, 2).astype(np.uint8),
        'learning_rate': np.linspace(0.5, 1.5, 2),
    },
    LGBMRegressor: {
        'n_estimators': np.linspace(75, 125, 2).astype(np.uint8),
        'learning_rate': np.linspace(0.5, 1.5, 2),
    },
    ExtraTreesRegressor: {
        'n_estimators': np.linspace(75, 150, 3).astype(np.uint8),
    },
}
