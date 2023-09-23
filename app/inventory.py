from app import db
from app.models import Dish

def check_inventory(dish_id, quantity):
    try:
        # Query the database to get the dish by ID
        dish = Dish.query.get(dish_id)

        # Check if the dish exists and if there is enough inventory
        if dish and dish.quantity >= quantity:
            return True
        else:
            return False
    except Exception as e:
        # Handle database errors or other exceptions as needed
        return False
