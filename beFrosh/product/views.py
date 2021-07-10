import io

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from rest_framework.parsers import JSONParser

from product.models import Product, ProductImage

@login_required(login_url='/seller/become-seller/')
def addProduct(request):
    
    user = request.user

    if request.method == 'GET':
 
        user_data = {'full_name': user.get_full_name()}

        return render(request, 'product/add_new.html', context={'user_data': user_data})

    elif request.method == 'POST':

        msg = ''
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        print(data)
        
        product_defaults = {
            'title': data['title'],
            'desk': data['desk'],
            'price': data['price'],
            'quality': data['quality'],
            'catagory': data['catagory']
        }

        try:
            product_, p_created = Product.objects.create(seller=user.seller, defaults=product_defaults)
            msg = 'PRODUCT ADDEDD SUCCESSFULLY'
            print(msg, p_created)
        except Exception as e:
            msg = 'PRODUCT NOT ADDEDD'
            print(e, msg)

        if p_created:

            image_defaults = {
                'img': None
            }

        try:
            img, i_created = ProductImage.objects.create(product=product_, defaults=image_defaults)
            msg = 'PRODUCT IMAGES ADDEDD SUCCESSFULLY'
            print(msg, i_created)
        except Exception as e:
            msg = 'PRODUCT IMAGES NOT ADDEDD'
            print(e, msg)

        return render(request, 'seller/account.html', context={'Message': msg})
