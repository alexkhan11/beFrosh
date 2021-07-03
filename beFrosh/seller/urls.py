from django.urls import path
from seller.views import createSeller
app_name = 'seller'

urlpatterns = [
    path('become-seller/', createSeller,name='become-seller'),

]
