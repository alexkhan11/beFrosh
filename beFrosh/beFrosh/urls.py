"""beFrosh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from mainApp.views import home
=======
from django.urls import path
from mainApp.views import home, createSeller, loginView, createUser, addProduct
>>>>>>> 0a34568c953d478bb51ef7c8cac644a58ef6c390

urlpatterns = [


    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', home),
    path('seller/',include('seller.urls'))
    # path('becomeSeller/', createSeller),
    # path('loginView/', loginView),
    # path('register/', createUser)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('',home),
    path('becomeSeller/', createSeller),
    path('loginView/', loginView),
    path('register/', createUser),
    path('addListing/', addProduct),
]
>>>>>>> 0a34568c953d478bb51ef7c8cac644a58ef6c390
