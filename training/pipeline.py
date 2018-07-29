from selectors import DataFrameColumnSelector
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def build_scaler_pipeline(field_name):
    return Pipeline(steps=[
        ('get_{0}'.format(field_name), DataFrameColumnSelector([field_name])),
        ('{0}_Scaler', StandardScaler())
    ])


def build_pipeline(X):
    '''
    Takes the training dataframe, and returns a pipeline with a model.
    '''
    return Pipeline(steps=[
        ('preprocessing', FeatureUnion(
            [(x, build_scaler_pipeline(x)) for x in X.columns])),
        ('model', LogisticRegression())
    ])
