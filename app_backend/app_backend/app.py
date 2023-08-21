from flask import Flask, render_template
from app_backend.food_facility import FoodFacilityList
import json

app = Flask(__name__)

@app.route('/')
def table():
    food_truck_searcher = FoodFacilityList()
    food_trucks = food_truck_searcher.get_approved_trucks()
    headings = list(food_trucks[0].keys())
    return render_template("table.html", headings=headings, data=food_trucks)

@app.route('/active_food_trucks')
def active_trucks():
    food_truck_searcher = FoodFacilityList()
    food_trucks = food_truck_searcher.get_approved_trucks()
    return food_trucks

@app.route('/all_food_trucks')
def all_trucks():
    food_truck_searcher = FoodFacilityList()
    food_trucks = food_truck_searcher.get_all_rows()
    return food_trucks

if __name__ == "__main__":
    app.run(debug=True) # this is a development server run not a production level deployment