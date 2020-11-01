from django.contrib.auth.models import AbstractUser
from django.db import models

"""
Описание моделей 
"""


class MyUser(AbstractUser):
    cash = models.FloatField(max_length=10)  # сумма денег у пользователя


class Product(models.Model):
    item = models.PositiveIntegerField(null=False, unique=True)  # раздел
    price = models.DecimalField(max_digits=8, decimal_places=2)  # цена
    in_stock = models.BooleanField()  # на складе остаток
    description = models.CharField(max_length=500)  # описание
    image = models.CharField(max_length=500)  # картинка

    def __str__(self):
        return str(self.item)


class Image(models.Model):
    image = models.CharField(max_length=500)
    product = models.ForeignKey(Product, related_name='images', on_delete='')
