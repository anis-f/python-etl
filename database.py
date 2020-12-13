from config import *
import psycopg2

class Database:
    def __init__(self):
        self.cursor = self.connect()

    def connect(self):
        conn = None
        try:
            config = Config()
            db_conf = config.get_db_conf()
            params = db_conf
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            return cur
        except (Exception, psycopg2.DatabaseError) as error:
            raise error

    def get_cursor(self):
        return self.cursor

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
