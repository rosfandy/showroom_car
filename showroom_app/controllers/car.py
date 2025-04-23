from ..models import Car
import logging
from decimal import Decimal
import uuid


def get_all_cars():
    cars = Car.objects.all()
    return cars


def add_new_car(new_car_data):
    try:
        car = Car(
            id=uuid.uuid4(),
            brand=new_car_data["brand"],
            model=new_car_data["model"],
            year=new_car_data["year"],
            base_price=new_car_data["base_price"],
            image_url=new_car_data["image_url"],
            loan_amount=new_car_data.get("loan_amount", None),
            interest_rate=new_car_data.get("interest_rate", None)
        )
        car.save()
    except Exception as e:
        print(f"Error saving car: {e}")
