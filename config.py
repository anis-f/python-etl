from configparser import ConfigParser

class Config:
    def __init__(self):
        self.db_conf = self.load_db_config()

    def load_db_config(self, section='postgresql'):
        parser = ConfigParser()
        parser.read('conf/database.ini')
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception(f'Section {section} not found in the {self} file')
        return db

    def get_db_conf(self):
        return self.db_conf

