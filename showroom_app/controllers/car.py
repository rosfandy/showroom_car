from ..models import Car, CarService
from decimal import Decimal
from django.shortcuts import render, get_object_or_404

import logging
import uuid


def get_all_cars():
    cars = Car.objects.all()
    return cars


def get_car_service(car):
    return CarService.objects.filter(car=car)


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


def add_new_car_services(service_data):
    try:
        print(service_data)
        new_service = CarService(
            id=uuid.uuid4(),
            car_id=service_data["car_id"],
            service_date=service_data["service_date"],
            description=service_data["description"],
            service_cost=service_data["service_cost"]
        )
        new_service.save()
    except Exception as e:
        print(f"Error saving car service: {e}")


def get_car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    if car.loan_amount and car.interest_rate:
        loan_amount = car.loan_amount
        interest_rate = car.interest_rate / 100
        interest_amount = loan_amount * interest_rate
    else:
        interest_amount = 0.0
        loan_amount = 0
        interest_rate = 0

    services = get_car_service(car)
    total_service_cost = sum(service.service_cost for service in services)

    try:
        if (loan_amount + interest_amount) > 0:
            hpp = round(
                (car.base_price / (loan_amount + interest_amount)) +
                total_service_cost,
                2
            )
        else:
            hpp = 0.0
    except Exception as e:
        print(f"Error calculating HPP: {e}")
        hpp = 0.0

    if car.loan_amount and car.interest_rate:
        monthly_installment = round(
            (loan_amount + interest_amount) / 12, 2
        )
    else:
        monthly_installment = 0.0

    return {
        'car': car,
        'services': services,
        'monthly_installment': monthly_installment,
        'hpp': hpp,
    }


def delete_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        car.delete()
        return {
            'success': True
        }

    except Exception as e:
        print(f"Error : {e}")
