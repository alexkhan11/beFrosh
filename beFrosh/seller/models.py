from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User



# Create your models here.
class Seller (models.Model):
    photo =  models.ImageField(null=True)
    phone = models.IntegerField()
    phone_2 = models.IntegerField()
    rating = models.FloatField()
    root_user = models.OneToOneField(User, on_delete=models.CASCADE)

# class Customer (models.Model):
#     user_name = models.CharField(unique=True, max_length=128)
#     full_name = models.CharField(max_length=128)
#     email = models.EmailField()
#     password = models.CharField(max_length=128)
