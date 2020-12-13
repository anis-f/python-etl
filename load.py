import pandas as pd
from database import Database



class Load:
    def __init__(self):
        try:
            self.db = Database()
        except Exception as e:
            raise Exception('Connection attempted to Database and failed!')

    def insert_into_db(self, data):
        try:
            data.apply(lambda row: self.execute_query(row),axis=1)
        except Exception as e:
            raise Exception('Error while inserting records into DB')

    def read_from_db(self):
        pass

    def execute_query(self, row):
        query = 'insert into records (day, status) values (\'{day}\', \'{status}\')'
        #print(query.format(day=row['Date'], status=row['status']))
        self.db.get_cursor().execute(query.format(day=row['Date'], status=row['status']))
        self.db.get_cursor().execute('COMMIT')
