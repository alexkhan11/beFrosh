from django.contrib import admin
from product.models import Product, FaveProduct


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class FaveProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(FaveProduct, FaveProductAdmin)
