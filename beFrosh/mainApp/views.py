from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):

    return render(request, 'index.html')


@login_required(login_url='/loginView/')
def createSeller(request):
    
    return render(request, 'account.html')



def loginView(request):

    return render(request, 'login.html')


def createUser(request):

    return render(request, 'signup.html')

