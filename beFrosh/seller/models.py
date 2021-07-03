from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Location (models.Model):
    country = models.CharField(max_length=128)
    province = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    address_line = models.CharField(max_length=128)

class Seller (models.Model):
    photo =  models.ImageField(null=True)
    phone_no = models.IntegerField()
    whatsapp_no = models.IntegerField(null=True)
    rating = models.FloatField()
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Location, on_delete=CASCADE)

# class Seller (models.Model):
#     photo =  models.ImageField(null=True)
#     phone = models.IntegerField()
#     phone_2 = models.IntegerField()
#     rating = models.FloatField()
#     root_user = models.OneToOneField(User, on_delete=models.CASCADE)

# class Customer (models.Model):
#     user_name = models.CharField(unique=True, max_length=128)
#     full_name = models.CharField(max_length=128)
#     email = models.EmailField()
#     password = models.CharField(max_length=128)
