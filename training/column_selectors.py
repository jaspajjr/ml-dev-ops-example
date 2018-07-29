from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class DataFrameColumnSelector(BaseEstimator, TransformerMixin):
    """
    Transformer class to select a single column from a pandas dataframe
    """
    def __init__(self, attribute_names):
        assert isinstance(attribute_names, list)
        assert len(attribute_names) == 1
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        assert isinstance(X, pd.DataFrame)
        return X[self.attribute_names].values.reshape(-1, 1)
