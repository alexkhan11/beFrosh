from django.shortcuts import render
from product.models import Product



def home(request):

    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'mainApp/index.html')

