from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)

