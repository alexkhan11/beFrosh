from django.contrib import admin
from product.models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductImage, ProductImageAdmin)