from django.contrib.auth.models import User
from django.db.models import fields

from rest_framework import serializers

from .models import Seller, Location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 
            'password'
        )