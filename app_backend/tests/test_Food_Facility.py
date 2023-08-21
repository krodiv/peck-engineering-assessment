from app_backend.food_facility import FoodFacilityList

class TestFoodTruck():

    def test_seed_db(self):
        try:
            food_stuff = FoodFacilityList()
            food_stuff.seed_database()
        except:  # not a good practice would be better to have a specific error caught or a list of them
            print("there was an error with backend seeding")
            assert False

    def test_get_all_rows(self):
        food_stuff = FoodFacilityList()
        food_trucks = food_stuff.get_all_rows()

        assert len(food_trucks) == 629

    def test_get_all_approved_trucks(self):
        food_stuff = FoodFacilityList()
        food_trucks = food_stuff.get_approved_trucks()

        assert len(food_trucks) == 60