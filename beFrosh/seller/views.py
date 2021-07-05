import io

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from rest_framework.parsers import JSONParser

from seller.models import Seller, Location


def loginView(request):

    if request.method == 'GET':
        return render(request, 'seller/login.html')
    
    elif request.method == 'POST':

        # print(request.body)

        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        print(data)

        username = data['username']
        password = data['password']
        
        msg = ''

        if not request.user.is_authenticated:
            
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                print("LOGIN SUCCESSFULL")
                return HttpResponseRedirect('seller/become-seller/')
                
            else:
                msg = 'Username or Password is Incorrect!'
                print(msg)
                return render (request,'seller/login.html', context={'Error': True, 'message': msg})
                
        else:
            print("User is authenticated")
            return HttpResponseRedirect('seller/become-seller/')

    # return render(request, 'seller/login.html')


@login_required(login_url='/seller/login/')
def createSeller(request):

    if request.method == 'GET':
        user = request.user

        full_name = user.get_full_name()
        user_data = {'full_name': full_name, 'email': user.email, 'username': user.username}

        # print(user_data)
        return render(request, 'seller/account.html', context={'user_data': user_data})

    elif request.method == 'POST':

        # print(request.body)

        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        print(data)

        try:
            location = Location(country=data['country'], province=data['province'], 
                district=data['district'], region=data['region'], address_line=data['address_line'])
            location.save()
            print("LOCATION ADDEDD SUCCESS")
        except Exception as e:
            print(e)


        try:
            seller = Seller(photo=None, phone_no=data['phone_no'], whatsapp_no=data['whatsapp_no'], 
                rating=0, user_name=request.user, address=location)
            seller.save()
            print("SELLER ADDEDD SUCCESS")
        except Exception as e:
            print(e)

        return HttpResponseRedirect('product/add-listing/')


def createUser(request):

    if request.method == 'GET':
        return render(request, 'seller/signup.html')

    elif request.method == 'POST':

        # print(request.body)

        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        print(data)
        
        msg = ''

        if data['password'] != data['r_password']:
            msg = "Password didn't Match"
            print(msg)
            return render (request, 'seller/signup.html', context={'Error': True, 'message': msg})
            
        f_name = data['first_name']
        l_name = data['last_name']
        
        try:
            user = User.objects.create_user(data['username'], data['email'], data['password'], first_name=f_name, last_name=l_name)
            print("USER CREATED SUCCESFULLY")	
            
        except Exception as e:
            msg = "Username already exists"
            print(msg)
            return render (request,'seller/signup.html', context={'Error': True, 'message': msg})
            
        user.save()
        login(request, user)
        print("LOGIN SUCCESS")
        
        return HttpResponseRedirect('/')


    # return render(request, 'seller/signup.html')

