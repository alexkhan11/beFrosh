import io
import json
import os
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from rest_framework.parsers import JSONParser

from seller.models import Seller, Location


@login_required(login_url='/seller/login/')
def logout_(request):
    logout(request)
    return HttpResponseRedirect('/seller/login/')


def loginView(request):
    success_url = 'http://127.0.0.1:8000/seller/become-seller/'

    if request.user.is_authenticated:
        return redirect('seller:become-seller')

    if request.method == 'GET':
        return render(request, 'seller/login.html')

    elif request.method == 'POST':
        # stream = io.BytesIO(request.body)
        # data = JSONParser().parse(stream)
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        msg = ''

        if not request.user.is_authenticated:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                resp = {'error': False, 'message': "LOGIN SUCCESSFULL",
                        'success_url': success_url}
                return JsonResponse(resp)

            else:
                msg = 'Username or Password is Incorrect!'
                resp = {'error': True, 'message': msg}
                return JsonResponse(resp)

        else:
            resp = {'error': False,
                    'success_url': success_url}
            return JsonResponse(resp)


@login_required(login_url='/seller/login/')
def changePassword(request):
    success_url = 'http://127.0.0.1:8000/seller/become-seller/'

    if request.method == 'GET':
        return render(request, 'seller/changepass.html')
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user

        current_password = data['current_password']
        new_password = data['new_password']
        confirm_password = data['confirm_password']

        if user.check_password(current_password):

            if confirm_password != new_password:
                resp = {'error': True, 'message': "Password didn't Match"}
                return JsonResponse(resp)

            else:
                user.set_password(new_password)
                user.save()
                resp = {'error': False, 'message': "Password Changed",
                        "success_url": success_url}
                return JsonResponse(resp)

        else:
            resp = {'error': True, 'message':  "Your Current Incorrect Password"}
            return JsonResponse(resp)


@ login_required(login_url='/seller/login/')
def createSeller(request):

    if request.method == 'GET':
        user = request.user
        full_name = user.get_full_name()
        is_seller = True

        try:
            seller = Seller.objects.get(user_name=user)
            location = seller.address
        except Seller.DoesNotExist:
            is_seller = False

        if is_seller:
            user_data = {
                'full_name': full_name,
                'email': user.email,
                'username': user.username,
                'address_line': location.address_line,
                'country': location.country,
                'province': location.province,
                'region': location.region,
                'district': location.district,
                'phone_no': seller.phone_no,
                'whatsapp_no': seller.whatsapp_no,
                'rating': seller.rating
            }
        else:
            user_data = {
                'full_name': full_name,
                'email': user.email,
                'username': user.username,
            }

        return render(request, 'seller/account.html', context={'user_data': user_data})

    elif request.method == 'POST':
        data = json.loads(request.body)

        location_defaults = {
            'country': data['country'],
            'province': data['province'],
            'district': data['district'],
            'region': data['region'],
            'address_line': data['address_line']
        }

        try:
            location, l_created = Location.objects.update_or_create(
                seller__user_name=request.user, defaults=location_defaults)

        except Exception as e:
            return JsonResponse({'error': True, "message": 'Location Error'})

        seller_defaults = {
            'photo': request.user.seller.photo,
            'phone_no': data['phone_no'],
            'whatsapp_no': data['whatsapp_no'],
            'rating': 0,
            'user_name': request.user,
            'address': location
        }

        try:
            seller, s_created = Seller.objects.update_or_create(
                user_name=request.user, defaults=seller_defaults)
        except Exception as e:
            return JsonResponse({'error': True, "message": 'Seller Error'})

        return JsonResponse({'error': False, "message": 'Status Updated Successfully'})


def change_usrpic(request):
    if request.method == 'POST':

        usrpic = request.FILES.get('usrpic')
        file_ext = os.path.splitext(str(request.FILES.get('usrpic')))[1]
        supported_ext = ['.png', '.jpg', '.jpeg']

        if file_ext.lower() in supported_ext:
            seller = Seller.objects.get(user_name=request.user)
            seller.photo = usrpic
            seller.save()
            return JsonResponse({'is_updated': True})
        else:
            JsonResponse({"is_updated": False})


def createUser(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
        return render(request, 'seller/signup.html')

    elif request.method == 'POST':
        data = json.loads(request.body)

        for key in data:  # IF ANY OF DATA IS EMPTY
            if data[key] == '':
                resp = {'error-key': key, 'error': True,
                        'message': f'Empty {key} is not allowed'}
                return JsonResponse(resp)

        if data['password'] != data['r_password']:
            resp = {'error': True, 'message': 'Password didn\'t Match'}
            return JsonResponse(resp)

        f_name = data['first_name']
        l_name = data['last_name']

        try:
            user = User.objects.create_user(
                data['username'], data['email'], data['password'], first_name=f_name, last_name=l_name)
            resp = {'error': False,
                    'message': 'USER CREATED SUCCESFULLY', "success_url": '/'}

            return JsonResponse(resp)

        except Exception as e:
            resp = {'error': True, 'message': 'Username already exists'}
            return JsonResponse(resp)

        user.save()
        login(request, user)
        resp = {'error': False,
                'message': 'USER CREATED SUCCESFULLY', "success_url": '/'}
        return JsonResponse(resp)
