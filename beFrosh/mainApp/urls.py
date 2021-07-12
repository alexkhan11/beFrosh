from django.urls import path

from mainApp import views

app_name = 'mainApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_products, name='search-products')

]
