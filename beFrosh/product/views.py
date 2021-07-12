import io
import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from rest_framework.parsers import JSONParser

from product.models import Product, FaveProduct
from seller.models import Seller

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


@login_required(login_url='/seller/become-seller/')
def addProduct(request):

    user = request.user

    if request.method == 'GET':
        user_data = {'full_name': user.get_full_name()}

        return render(request, 'product/add_new.html', context={'user_data': user_data})

    elif request.method == 'POST':
        data = request.POST
        for key in data:
            if data[key] == '':

                resp = {'error': True,
                        'message': f'{key} Can\'t Be Empty', 'error-key': key}
                return JsonResponse(resp)
        try:
            product_ = Product.objects.create(
                title=data['title'], desc=data['desc'],
                price=data['price'], catagory=data['catagory'],
                image=request.FILES.get('product-pic'),
                seller=user.seller)
            product_.save()

        except Exception as e:
            resp = {'error': True, 'message': 'PRODUCT NOT ADDEDD'}
            return JsonResponse(resp)

        resp = {'error': False,
                'message': 'PRODUCT ADDEDD SUCCESSFULLY', "success_url": '/'}
        return JsonResponse(resp)


@login_required(login_url='/seller/become-seller/')
def check_it_later(request):
    if request.user.is_authenticated:

        product_id = json.loads(request.body).get('product_id')
        product = Product.objects.get(pk=product_id)
        seller = Seller.objects.get(user_name=request.user)
        is_fave = FaveProduct.objects.filter(product=product, seller=seller)

        if not is_fave:
            fave_roduct = FaveProduct.objects.create(
                product=product, seller=seller)
            return JsonResponse({'error': False, 'message': 'Added to Favorites'})
        else:
            return JsonResponse({'error': True, 'message': 'Already in favorites '})

    return JsonResponse({'error': True})


def my_listings(request):
    user = Seller.objects.get(user_name=request.user)
    products_set = Product.objects.filter(seller=user)
    products = serializers.serialize('json', products_set)

    return JsonResponse({'products': products})


def favorites(request):
    user = Seller.objects.get(user_name=request.user)
    products_set = FaveProduct.objects.filter(seller=user)
    products = []
    for fave_product in products_set:
        products.append({
            'fields': {
                'title': fave_product.product.title,
                'address': fave_product.product.product_add(),
                'desc': fave_product.product.desc,
                'price': fave_product.product.price,
                'seller': fave_product.product.seller.user_name.get_full_name(),
                'image': fave_product.product.image.name

            },
            'pk': fave_product.pk
        })
    return JsonResponse((products), safe=False)
