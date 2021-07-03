from django.shortcuts import render
from product.models import Product



def home(request):

    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'mainApp/index.html',context)


# @login_required(login_url='/loginView/')
# def createSeller(request):
    
#     if request.method == 'GET':
#         user = request.user

#         full_name = user.get_full_name()
#         user_data = {'full_name': full_name, 'email': user.email, 'username': user.username}
# <<<<<<< HEAD
# =======
# >>>>>>> 0a34568c953d478bb51ef7c8cac644a58ef6c390
# >>>>>>> c4ec0048a031c7c2d4d7494e37d8bddd5dd2f804

#         print(user_data)
#         return render(request, 'account.html', context={'user_data': user_data})

# <<<<<<< HEAD
# =======
# <<<<<<< HEAD
# def home(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'mainApp/index.html',context)
# =======
# >>>>>>> c4ec0048a031c7c2d4d7494e37d8bddd5dd2f804
#     elif request.method == 'POST':

#         print(request.body)

#         data = serializers.deserialize('json', request.body)

#         try:
#             location = Location.objects.create(data['country'], data['province'], data['district'], data['region'], data['address_line'])
        
#         except Exception as e:
#             print(e)

#         location.save()

#         try:
#             seller = Seller.objects.create(None, data['phone_no'], data['whatsapp_no'], 0, user_name=request.user, address=location)

#         except Exception as e:
#             print(e)
# <<<<<<< HEAD

#         seller.save()    

#         return HttpResponseRedirect('/addListing/')
# =======

#         seller.save()    
# >>>>>>> c4ec0048a031c7c2d4d7494e37d8bddd5dd2f804

#         return HttpResponseRedirect('/addListing/')

# <<<<<<< HEAD
# =======

# >>>>>>> c4ec0048a031c7c2d4d7494e37d8bddd5dd2f804
# ############## ADD PRODUCT ####################

# @login_required(login_url='/loginView/')
# def addProduct(request):

#     return render(request, 'add_new.html')


# ############### CREATE USER ###################
# def createUser(request):

#     if request.method == 'GET':
#         return render(request, 'signup.html')

#     elif request.method == 'POST':

#         print(request.body)
#         data = serializers.deserialize('json', request.body)
        
#         msg = ''

#         if data['password'] != data['r_password']:
#             msg = "Password didn't Match"
#             return render (request, 'signup.html', context={'Error': True, 'message': msg})
            
#         f_name = data['f_name']
#         l_name = data['l_name']
        
#         try:
#             user = User.objects.create_user(data['username'], data['email'], data['password'], first_name=f_name, last_name=l_name)	
            
#         except Exception as e:
#             msg = "Username already exists"
#             return render (request,'signup.html', context={'Error': True, 'message': msg})
            
#         user.save()
#         login(request, user)
        
#         return HttpResponseRedirect('/')



# ################# LOGIN FUNC ##################
# def loginView(request):

#     if request.method == 'GET':
#         return render(request, 'login.html')
    
#     elif request.method == 'POST':

#         print(request.body)
#         data = serializers.deserialize('json', request.body)

#         username = data['username']
#         password = data['password']
        
#         msg = ''

#         if not request.user.is_authenticated:
            
#             user = authenticate(request, username = username, password = password)
            
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('')
                
#             else:
#                 msg = 'Username or Password is Incorrect!'
#                 return render (request,'login.html', context={'Error': True, 'message': msg})
                
#         else:
#             print("User is authenticated")
#             return HttpResponseRedirect('/')





# >>>>>>> 0a34568c953d478bb51ef7c8cac644a58ef6c390
