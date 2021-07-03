from django.shortcuts import render

# Create your views here.
# @login_required(login_url='/loginView/')
def createSeller(request):
    
    return render(request, 'seller/account.html')
    
def loginView(request):

    return render(request, 'seller/login.html')


def createUser(request):

    return render(request, 'seller/signup.html')

