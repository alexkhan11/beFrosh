from django.urls import path
from django.contrib import admin
from seller.views import createSeller, loginView, createUser, logout_, changePassword

app_name = 'seller'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('become-seller/', createSeller, name='become-seller'),
    path('login/', loginView, name='login'),
    path('register/', createUser, name='register'),
    path('change-password/', changePassword, name='change-password'),
    path('logout/', logout_, name='logout'),

]
