from django.contrib import admin
from .models import Seller, Location, Product

# Register your models here.

class SellerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Seller, SellerAdmin)


# class CustomerAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Customer, CustomerAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)