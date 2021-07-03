from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from seller.models import Seller, Location

class Product (models.Model):
    title = models.CharField(null=False, max_length=128)
    desc =models.CharField(null=False, max_length=512)
    image= models.ImageField(upload_to='product-images')
    price = models.FloatField()
    quality = models.CharField(max_length=128)
    catagory = models.CharField(max_length=128)
    sold_status=models.BooleanField(default=False)
    
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=CASCADE)
    


