import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


def get_preprocessed_with_one_hot_enc(df: pd.DataFrame) -> pd.DataFrame:
    encoder = OneHotEncoder()
    cat_columns, num_columns = (
        df.select_dtypes(include=types).columns.tolist() for types in (np.object_, np.number)
    )
    encoder.fit(df[cat_columns])
    transformed = encoder.transform(df[cat_columns])
    cat_df = pd.DataFrame(transformed.toarray(), columns=encoder.get_feature_names_out(cat_columns))
    return pd.concat([cat_df, df[num_columns]], axis=1)


def get_preprocessed_with_label_enc(series: pd.Series) -> pd.Series:
    encoder = LabelEncoder()
    res = pd.Series(encoder.fit_transform(series))
    return res
