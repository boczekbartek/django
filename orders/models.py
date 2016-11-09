from django.db import models
from django.utils import timezone
import datetime


# class Order(models.Model):
#     dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
#     order_number = models.PositiveIntegerField()
#     date = models.CharField(max_length=20)


class Sauce(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' ' + str(self.price) + self.image

class Pasta(models.Model):
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return 'Pasta type' + self.type

class Additional_Ingredient (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isChoosen = models.BooleanField()
    image = models.CharField(max_length=1000)

class Dish(models.Model):
    pasta = models.ForeignKey(Pasta, default=None)
    sauce = models.ForeignKey(Sauce, default=None)
    addIngredients = models.ManyToManyField(Additional_Ingredient,symmetrical=False)
    totalPrice = models.DecimalField(max_digits=5, decimal_places=2)
    orderTime = models.DateTimeField(auto_now=True)
    deliveryTime = models.DateTimeField(default=timezone.now)

class Delivery(models.Model):
    f_delivery_time = models.DecimalField(max_digits=4, decimal_places=2, default=10.00)
    l_delivery_time = models.DecimalField(max_digits=4, decimal_places=2, default=18.00)
    delvs_per_hour = models.IntegerField(default=2)

