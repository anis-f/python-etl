import pandas as pd
import requests
import json


class Extract:
    def __init__(self):
        self.data_sources = json.load(open('conf/sources.json'))
        self.api = self.data_sources['data_sources']['api']
        self.csv = self.data_sources['data_sources']['csv']

    def get_api_data(self, api_name):
        api_url = self.api[api_name]
        response = requests.get(api_url)
        return response.json()

    def get_csv_data(self, csv_name):
        df = pd.read_csv(self.csv[csv_name])
        return df

    def get_google_bigquery_data(self, query_url):
        pass
