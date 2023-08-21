import requests

class TestEndpoints:

    def test_get_all_active_food_institutions(self):
        res = requests.get(
            'http://127.0.0.1:5000/active_food_trucks'
        )
        print("trying out the thing")
        print(res.json())

        assert len(res.json()) == 60

    def test_get_all_food_institutions(self):
        res = requests.get(
            'http://127.0.0.1:5000/all_food_trucks'
        )
        print("trying out the thing")
        print(res.json())

        assert len(res.json()) == 629
