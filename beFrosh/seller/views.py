import io
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
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

@login_required(login_url='/seller/login/')
def changePassword(request):

	if request.method == 'POST':
		data = json.loads(request.body)
		user = request.user

		current_password = data['password']
		new_password = data['new_password']
		confirm_password = data['confirm_password']

		if user.check_password(current_password):

			if confirm_password != new_password:
				msg = "Password didn't Match"
				return HttpResponse(json.dumps({'success': False, 'message': msg}), status=403)

			else:
				msg = "Password Changed"
				user.set_password(new_password)

				return HttpResponse(json.dumps({'success': True, 'message': msg}), status=200)

		else:
			msg = "Incorrect Password"
			return HttpResponse(json.dumps({'success': False, 'message': msg}), status=403)

	else: 

		return HttpResponse(status=405)

@login_required(login_url='/seller/login/')
def createSeller(request):

    if request.method == 'GET':
        user = request.user
        full_name = user.get_full_name()
        is_seller = True

        try:
            seller = Seller.objects.get(user_name = user)
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

        msg = ''
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        print(data)
        
        location_defaults = {
            'country': data['country'],
            'province': data['province'],
            'district': data['district'],
            'region': data['region'],
            'address_line': data['address_line']
        }

        try:
            location, l_created = Location.objects.update_or_create(seller__user_name=request.user, defaults=location_defaults)
            print("LOCATION ADDEDD SUCCESS", l_created)
        except Exception as e:
            print(e)

        seller_defaults = {
            'photo': None,
            'phone_no': data['phone_no'],
            'whatsapp_no': data['whatsapp_no'],
            'rating': 0,
            'user_name': request.user,
            'address' : location
        }
        
        try:
            seller, s_created = Seller.objects.update_or_create(user_name=request.user, defaults=seller_defaults)
            msg = 'Account Updated Successfully'
            print("SELLER ADDEDD SUCCESS", s_created)
        except Exception as e:
            msg = 'An Error Occured, Please try agian'
            print(e)

        return render(request, 'seller/account.html', context={'Message': msg})


def createUser(request):

    if request.method == 'GET':
        return render(request, 'seller/signup.html')

    elif request.method == 'POST':

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


