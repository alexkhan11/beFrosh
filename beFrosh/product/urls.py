from django.urls import path
from product.views import addProduct

app_name='product'

urlpatterns=[
    path('add-listing/', addProduct, name='add-listing'),
]