from django.db import models


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
