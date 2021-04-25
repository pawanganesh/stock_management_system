from django.db import models


class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name
