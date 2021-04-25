from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    is_digital = models.BooleanField(default=False)


class Supplier(models.Model):
    pass
