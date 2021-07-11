import io

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from rest_framework.parsers import JSONParser

from product.models import Product




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
