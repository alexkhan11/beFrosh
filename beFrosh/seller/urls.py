from django.urls import path
from seller.views import createSeller, loginView, createUser

app_name = 'seller'

urlpatterns = [
    path('become-seller/', createSeller, name='become-seller'),
    path('login/', loginView, name='login'),
    path('register/', createUser, name='register'),

]
