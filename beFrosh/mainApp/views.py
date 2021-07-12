from django.shortcuts import render
from product.models import Product
from django.http import JsonResponse

from django.db.models import Q
import json


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'mainApp/index.html', context)


def search_products(request):
    data = json.loads(request.body)
    search_text = data.get('search_text')
    catagory = data.get('catagory')
    products_set = {}
    products = []

    if search_text:
        products_set = Product.objects.filter(
            Q(title__contains=search_text) |
            Q(desc__contains=search_text) &
            Q(sold_status=False))

    if catagory:
        products_set = Product.objects.filter(
            Q(catagory=catagory) &
            Q(sold_status=False))

    for product in products_set:
        products.append({
            'fields': {
                'title': product.title,
                'address': product.product_add(),
                'desc': product.desc,
                'price': product.price,
                'seller': product.seller.user_name.get_full_name(),
                'image': product.image.name

            },
            'pk': product.pk
        })

    return JsonResponse(products, safe=False)
