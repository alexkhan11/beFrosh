from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Seller (models.Model):
    photo =  models.ImageField(null=True)
    phone = models.IntegerField()
    phone_2 = models.IntegerField()
    rating = models.FloatField()
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey("Location", on_delete=CASCADE)


# class Customer (models.Model):
#     user_name = models.CharField(unique=True, max_length=128)
#     full_name = models.CharField(max_length=128)
#     email = models.EmailField()
#     password = models.CharField(max_length=128)


class Location (models.Model):
    country = models.CharField(max_length=128)
    province = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    house_no = models.IntegerField()

class Product (models.Model):
    title = models.CharField(null=False, max_length=128)
    des =models.CharField(null=False, max_length=512)
    image= models.ImageField()
    price = models.FloatField()
    quality = models.CharField(max_length=128)
    catagory = models.CharField(max_length=128)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=CASCADE)



