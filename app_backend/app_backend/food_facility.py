from dataclasses import dataclass, asdict
from app_backend.connection.db_connection import DbConnection, FoodTruck
from sqlalchemy.orm import sessionmaker
import os.path
import pandas as pd


# dataclass food facility
@dataclass
class FoodFacility:
    """Class for each given row in food facility"""
    applicant: str = None
    address: str = None
    permit: str = None
    status: str = None
    food_items: list = None
    latitude: float = None
    longitude: float = None
    zip: int = None

    def dataclass_to_json(self):
        # get data as dictionary
        return asdict(self)

@dataclass
class FoodFacilityList:

    food_facilities: [FoodFacility]
    def __init__(self):
        self.seed_database()
        self.food_facilities = []

    # can add more functions that return helpful information to the user
    # like locations, food types, etc

    def create_food_facility_list(self, query_results):
        for food_truck in query_results:
            food_facility = FoodFacility(
                food_truck.applicant,
                food_truck.permit,
                food_truck.address,
                food_truck.status,
                food_truck.food_items,
                food_truck.latitude,
                food_truck.longitude,
                food_truck.zip,
            )
            self.food_facilities.append(food_facility.dataclass_to_json())
        return query_results

    def get_all_rows(self):
        food_trucks = FoodTruck.query.all()  # add a close connection method
        self.create_food_facility_list(food_trucks)
        sessionmaker.close_all()
        return self.food_facilities

    def get_approved_trucks(self):
        approved_trucks = FoodTruck.query.where(FoodTruck.status == 'APPROVED')
        self.create_food_facility_list(approved_trucks)
        sessionmaker.close_all()
        return self.food_facilities

    # This function is ment to seed the database with csv file data
    def seed_database(self, file_path=None):
        def replace_colon(value):
            try:
                if ": " in value:
                    value = value.split(": ")
                else:
                    value = [value]
            except:
                print(f"had an error with: {value}")
            return value
        file_path = os.path.join(os.path.dirname(__file__), "Mobile_Food_Facility_Permit.csv")
        df_csv = pd.read_csv(file_path)

        applicable_columns = df_csv[
            ['Applicant', 'Address', 'permit', 'Status', 'FoodItems', 'Latitude', 'Longitude', 'Zip Codes']
        ]
        applicable_columns\
            .columns = ['applicant', 'permit', 'address', 'status', 'food_items', 'latitude', 'longitude', 'zip']

        applicable_columns.to_sql(
            'food_truck',
            con=DbConnection().get_engine(),
            index=True,
            index_label='id',
            if_exists='replace'
        )
        sessionmaker.close_all()
