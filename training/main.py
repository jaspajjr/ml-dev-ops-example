import pandas as pd


def load_data():
    '''
    Loads the data for training the model.
    '''
    df = pd.read_csv('/data/iris.csv')
    return df


def main():
    df = load_data()
    print(df)


if __name__ == '__main__':
    main()
