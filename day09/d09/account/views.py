from django.http import Http404, HttpResponse 
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
import json
# Create your views here.

def home(request):
    auth.logout(request)
    return render(request, "home.html")

def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        print('aaaaaaaa',username)
        print('aaaaaaaa',password)
        # User.objects.create_user(username, None, password)
        user = auth.authenticate(username=username,
            password=password)
        if user and user.is_active:
            auth.login(request, user)
            data = json.dumps({
                "error_login": "",
                "logged": "Logged as "+username,
            })
            return HttpResponse(data, content_type="application/json")

        else:
            data = json.dumps({
                'error_login': 'Wrong username or password'
            })
            return HttpResponse(data, content_type="application/json")
        return HttpResponse(content_type="application/json")
    else:
        raise Http404

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logout')
        data = json.dumps({})
        return HttpResponse(data, content_type="application/json")
    else:
        raise Http404


# def populate(request):
#     try:
        
#         return HttpResponse('OK')
#     except ValueError as e:
#         return HttpResponse('Error :',e)