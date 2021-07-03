from django.contrib import admin
from .models import  Location, Product

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)