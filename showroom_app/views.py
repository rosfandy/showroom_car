from showroom_app.controllers.car import add_new_car, get_all_cars, get_car_detail, add_new_car_services, delete_car
from decimal import Decimal
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Car  


def home(request):
    cars = get_all_cars()
    return render(request, 'home.html', {"cars": cars})


@csrf_exempt
def add_cars(request):
    if request.method == 'POST':
        def safe_decimal(value):
            return Decimal(value) if value and value.strip() != '' else Decimal('0.0')

        new_car = {
            "brand": request.POST.get('brand'),
            "model": request.POST.get('model'),
            "year": int(request.POST.get('year')),
            "base_price": safe_decimal(request.POST.get('base_price', '0.0')),
            "image_url": request.POST.get('image_url'),
            "loan_amount": safe_decimal(request.POST.get('loan_amount', '0.0')),
            "interest_rate": safe_decimal(request.POST.get('interest_rate', '0.0'))
        }

        add_new_car(new_car)

        return redirect('home')

    return render(request, 'add_cars.html')


def car_detail(request, car_id):
    if request.method == 'POST':
        service = {
            "car_id": car_id,
            "service_date": request.POST.get('service_date'),
            "description": request.POST.get('description'),
            "service_cost": request.POST.get('service_cost')
        }
        add_new_car_services(service)
        return redirect('car_detail', car_id=car_id)
    datas = get_car_detail(request, car_id)
    return render(request, 'detail_cars.html', datas)


def delete_car(request, car_id):
    if request.method == 'POST':
        car = Car.objects.get(id=car_id)
        car.delete()
        return redirect('home')
