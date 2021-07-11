from django.urls import path
from django.contrib import admin
from product.views import addProduct

app_name = 'product'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-listing/', addProduct, name='add-listing'),

]
