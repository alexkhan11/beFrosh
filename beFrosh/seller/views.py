import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect 
from django.db import close_old_connections
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from seller.models import Seller, Location




# Create your views here.
# @login_required(login_url='/login/')
def createSeller(request):

    if request.method == 'GET':
        user = request.user

        full_name = user.get_full_name()
        user_data = {'full_name': full_name, 'email': user.email, 'username': user.username}
        print(user_data)
        return render(request, 'seller/account.html', context={'user_data': user_data})

    elif request.method == 'POST':

        print(request.body)

        data = serializers.deserialize('json', request.body)

        try:
            location = Location.objects.create(data['country'], data['province'], data['district'], data['region'], data['address_line'])
        
        except Exception as e:
            print(e)

        location.save()

        try:
            seller = Seller.objects.create(None, data['phone_no'], data['whatsapp_no'], 0, user_name=request.user, address=location)

        except Exception as e:
            print(e)

        seller.save()    

        return HttpResponseRedirect('/addListing/')

    


def loginView(request):

    if request.method == 'GET':
        return render(request, 'seller/login.html')
    
    elif request.method == 'POST':

        print(request.body)
        data = serializers.deserialize('json', request.body)

        username = data['username']
        password = data['password']
        
        msg = ''

        if not request.user.is_authenticated:
            
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('')
                
            else:
                msg = 'Username or Password is Incorrect!'
                return render (request,'seller/login.html', context={'Error': True, 'message': msg})
                
        else:
            print("User is authenticated")
            return HttpResponseRedirect('/')

    # return render(request, 'seller/login.html')


def createUser(request):

    if request.method == 'GET':
        return render(request, 'seller/signup.html')

    elif request.method == 'POST':

        print(request.body)
        data = serializers.deserialize('json', request.body)
        
        msg = ''

        if data['password'] != data['r_password']:
            msg = "Password didn't Match"
            return render (request, 'seller/signup.html', context={'Error': True, 'message': msg})
            
        f_name = data['f_name']
        l_name = data['l_name']
        
        try:
            user = User.objects.create_user(data['username'], data['email'], data['password'], first_name=f_name, last_name=l_name)	
            
        except Exception as e:
            msg = "Username already exists"
            return render (request,'seller/signup.html', context={'Error': True, 'message': msg})
            
        user.save()
        login(request, user)
        
        return HttpResponseRedirect('/')


    # return render(request, 'seller/signup.html')

