from dataclasses import dataclass, asdict

# dataclass food facility
@dataclass
class FoodFacility:
    """Class for each given row in food facility"""
    name: str
    address: str
    permit_status: bool
    food_items: list
    latitude: float
    longitude: float
    zip: int

    def dataclass_to_json(self):
        # get data as dictionary
        return asdict(self)

    def seed_database(self):
        # seed database
        pass

# declare types of food values

# search for given values by food type and open?
# return useful info for a user

#