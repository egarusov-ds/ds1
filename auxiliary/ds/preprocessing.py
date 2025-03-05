import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


def get_preprocessed_with_one_hot_enc(df: pd.DataFrame) -> pd.DataFrame:
    encoder = OneHotEncoder()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    encoder.fit(df[categorical_columns])
    transformed = encoder.transform(df[categorical_columns])
    return pd.DataFrame(transformed.toarray(), columns=encoder.get_feature_names_out(categorical_columns))


def get_preprocessed_with_label_enc(series: pd.Series) -> pd.Series:
    encoder = LabelEncoder()
    res = pd.Series(encoder.fit_transform(series))
    print(dict(zip(encoder.classes_, encoder.transform(encoder.classes_))))
    return res
