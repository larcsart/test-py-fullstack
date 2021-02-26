from django.db import models
from django.core.validators import MinValueValidator


class Customers(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    city = models.CharField(max_length=255)
