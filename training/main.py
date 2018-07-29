import pandas as pd
from pipeline import build_pipeline
from sklearn.externals import joblib


def load_data():
    '''
    Loads the data for training the model.
    '''
    df = pd.read_csv('/data/iris.csv')
    return df


def fit_model(pipeline, X, y):
    '''
    Fits the provided pipeline.
    '''
    return pipeline.fit(X, y.values.ravel())


def persist_model(pipeline):
    '''
    Saves the pipeline to the results folder.
    '''
    joblib.dump(pipeline, '/results/pipeline.pkl')


def main():
    df = load_data()
    X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    y = df[['Species']]
    pipe = fit_model(build_pipeline(X), X, y)
    persist_model(pipe)


if __name__ == '__main__':
    main()
