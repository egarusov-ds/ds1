import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

TARGET_VAR = 'y'
TEST_RATIO = 0.2
FEATURES_COUNT = 20

CLASSIFIERS_TO_TEST = (
    AdaBoostClassifier,
    KNeighborsClassifier,
    DecisionTreeClassifier,
    RandomForestClassifier,
    DummyClassifier,
)

MAP_GRID_SEARCH_PARAMS = {
    'AdaBoostClassifier': {
        'n_estimators': np.linspace(30, 70, 3).astype(np.uint),
        'learning_rate': np.linspace(0.75, 1.25, 3),
    },
    'KNeighborsClassifier': {
        'n_neighbors': np.linspace(3, 7, 3).astype(np.uint),
        'weights': ('uniform', 'distance'),
    },
    'DecisionTreeClassifier': {
        'max_depth': (None, 3, 5),
    },
    'RandomForestClassifier': {
        'max_depth': (None, 3, 5),
    },
    'DummyClassifier': {
        'strategy': ('most_frequent', 'prior', 'stratified'),
    },
}
