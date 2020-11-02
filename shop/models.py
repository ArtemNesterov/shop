from django.contrib.auth.models import AbstractUser, User
from django.db import models

"""
Description of models 
"""


class MyUser(User):
    cash = models.DecimalField(max_digits=8, decimal_places=2)  # сумма денег у пользователя


class Image(models.Model):
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=False)

    def __str__(self):
        return str(self.product)


"""
Product(section) model
"""


class ItemType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


"""
Model of product description
"""


class Product(models.Model):
    count = models.PositiveIntegerField()  # количество товара
    item = models.ForeignKey(ItemType, on_delete=models.CASCADE)  # раздел
    price = models.DecimalField(max_digits=8, decimal_places=2)  # цена
    in_stock = models.BooleanField(default=True)  # на складе остаток
    description = models.CharField(max_length=500)  # описание
    image = models.ForeignKey(Image, related_name='product', on_delete=models.CASCADE)

    """
    Function to display the date and time when adding an item
    """

    def __str__(self):
        from datetime import datetime as datetime
        now = str(datetime.now())
        return '{}-{}'.format(self.item, now)
