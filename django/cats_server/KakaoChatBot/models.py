from django.db import models

# Create your models here.

class RestaurantInfo(models.Model):
    @staticmethod
    def name():
        return 'RestaurantInfo'
    @staticmethod
    def pk_name():
        return 'date'
    date = models.CharField(max_length=10)
    restaurantName = models.CharField(max_length=255)
    timeOfDay = models.CharField(max_length=255)
    menu = models.CharField(max_length=255)