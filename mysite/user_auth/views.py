from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# def user_login(request):
#     return render(request, 'login.html')

def user_logout(request):
    '''Sets the user session to a logout state.
    
    '''
    logout(request)
    return render(request, 'logout.html')

def user_login(request):
    '''Reads the entered username and password submitted on the login page and compares it to
        registered users. If the login credentials exist then the user is redirected back to the
        main page, otherwise sets the user as logged in for teh session.

        :param str username: Username. Case sensitive.
        :param str password: Password. Case sensitive
    
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request,'login.html')
        else:
            login(request, user)
            return render(request,'main.html')     
    return render(request,'login.html')
