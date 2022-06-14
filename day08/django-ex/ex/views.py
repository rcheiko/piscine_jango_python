from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse 
from .forms import FileForm


def home(request):
    try:
        files = File.objects.all()
        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        else:
            form = FileForm()
        return render(request, "home.html", {'form':form, 'files':files})
    except ValueError as e:
        return HttpResponse(e)
    return HttpResponse('erreur')