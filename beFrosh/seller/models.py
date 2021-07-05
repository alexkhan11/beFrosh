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

    def __str__(self) -> str:
        addr = self.address_line + " " + self.street + " " + self.region + " " + self.province
        return addr

class Seller (models.Model):
    photo =  models.ImageField(null=True)
    phone_no = models.IntegerField()
    whatsapp_no = models.IntegerField(null=True)
    rating = models.FloatField()
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Location, related_name='Location', on_delete=CASCADE)

    def __str__(self) -> str:
        return self.user_name

