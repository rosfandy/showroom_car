import uuid
from django.db import models


class Car(models.Model):
    id = models.CharField(primary_key=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    base_price = models.DecimalField(max_digits=15, decimal_places=2)
    loan_amount = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, blank=True)
    interest_rate = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarService(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='services')
    service_date = models.DateField()
    description = models.TextField()
    service_cost = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Service for {self.car} on {self.service_date}"
