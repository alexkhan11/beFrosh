from django.contrib import admin
from .models import Seller, Location

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)

class SellerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Seller, SellerAdmin)
