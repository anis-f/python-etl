import pandas as pd


def calculate_status(row):
    if row['PercentOfBaseline'] > 50:
        return 'OK'
    else:
        return 'NOT OK'


class Transform:
    def transform_data(self, data):
        if isinstance(data, pd.DataFrame):
            data['status'] = data.apply(lambda row: calculate_status(row), axis=1)
        return data