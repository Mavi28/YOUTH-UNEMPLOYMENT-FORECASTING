import pandas as pd

def preprocess(df):
    df = df.copy()

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)

    df['time_index'] = range(len(df))

    return df
