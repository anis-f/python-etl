from database import Database
from extract import Extract
from transform import Transform
from load import Load

if __name__ == '__main__':
    database_object = Database()
    extract = Extract()
    transform = Transform()
    load = Load()
    source_data = extract.get_csv_data('covid_impact_on_airport_traffic')
    transformed_data = transform.transform_data(source_data)
    load.insert_into_db(transformed_data)

