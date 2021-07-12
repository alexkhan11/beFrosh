from django.urls import path
from django.contrib import admin
from product.views import addProduct, check_it_later, my_listings, favorites

app_name = 'product'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-listing/', addProduct, name='add-listing'),
    path('check-it-later/', check_it_later, name='check-it-later'),
    path('my-listings/', my_listings, name='my-listings'),
    path('favorites/', favorites, name='favorites')
]
