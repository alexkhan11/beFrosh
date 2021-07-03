from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from seller.models import Seller


class Location (models.Model):
    country = models.CharField(max_length=128)
    province = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    house_no = models.IntegerField()

class Product (models.Model):
    title = models.CharField(null=False, max_length=128)
    desc =models.CharField(null=False, max_length=512)
    image= models.ImageField(upload_to='product-images')
    price = models.FloatField()
    quality = models.CharField(max_length=128)
    catagory = models.CharField(max_length=128)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=CASCADE)


    sold_status=models.BooleanField(default=False)


