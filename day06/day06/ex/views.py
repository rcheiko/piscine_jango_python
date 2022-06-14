from django import forms
from django.conf import settings
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from random import choice
from .registerForm import register
from .loginForm import login
from .models import tip_model
from .tipForm import tip_form
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import votes

def home(request):
    try:
        Tip = tip_model.objects.all()
        form_tip = tip_form()
        if request.user.is_authenticated:
            if (request.method == 'POST'):
                try:
                    form_tip = tip_form(request.POST)
                    if form_tip.is_valid():
                        form_tip.save()
                        form_tip = tip_form()
                        return render(request, 'home.html', {"username":request.user.username, "form":form_tip, "tip_content":Tip})
                    else:
                        form_tip = tip_form()
                        return render(request, 'home.html', {"username":request.user.username, "form":form_tip, "tip_content":Tip, "error_tip":"You have entered a wrong date"})
                except Exception as e:
                    form_tip = tip_form()
                    print('erreur', e)
                    return render(request, 'home.html', {"username":request.user.username, "form":form_tip, "tip_content":Tip})
            else:
                return render(request, 'home.html', {"username":request.user.username, "form":form_tip, "tip_content":Tip})
        random_name = request.COOKIES
        if "username" not in random_name:
            random_name = choice(settings.LIST_NAME)
            request.COOKIES['username'] = random_name
            response = render(request, 'home.html', {"username":random_name, "tip_content":Tip})
            response.set_cookie('username', random_name,42)
            return response
        random_name = random_name['username']
        return render(request, 'home.html', {"username":random_name, "tip_content":Tip})
    except Exception as e:
        return HttpResponse(e)

def login_fct(request):
    try:
        if request.user.is_authenticated:
            return redirect("/")
        try:
            if (request.method == 'POST'):
                form = login(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = auth.authenticate(username=username,
                                            password=password)
                    if user and user.is_active:
                        auth.login(request, user)
                        return redirect("/")
                    else:
                        form._errors['username'] = ['This user doesn\'t exist.']
            else:
                form = login()
        except Exception as e:
            print(e)
            return render(request, 'login.html', {"form":form})
        return render(request, 'login.html', {"form":form})
    except Exception as e:
        return HttpResponse(e)

def register_fct(request):
    try:
        if request.user.is_authenticated:
            return redirect("/")
        try:
            if (request.method == 'POST'):
                form = register(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    password_confirmation = form.cleaned_data['password_confirmation']
                    if (password != password_confirmation):
                        return render(request, 'register.html', {"form":form, "passwordNotMatch":"Password is not the same"})
                    User.objects.create_user(username, None, password)
                    user = auth.authenticate(username=username,
                                            password=password)
                    if user and user.is_active:
                        auth.login(request, user)
                        return redirect("/")
            else:
                form = register()
        except Exception as e:
            print (e)
            return render(request, 'register.html', {"form":form, "userExist":"Username Already Exist"})
        return render(request, 'register.html', {"form":form})
    except Exception as e:
        return HttpResponse(e)

@login_required
def upvotes(request, id):
    try:
        if len(votes.objects.filter(id_content=id, id_user=request.user.id)) != 0:
            if votes.objects.filter(id_content=id, id_user=request.user.id, up=True):
                votes.objects.filter(id_content=id, id_user=request.user.id).delete()
                tip_model.objects.filter(id=id).update(upvotes=F('upvotes')-1)
            return redirect("/")
        v = votes(id_content=id, id_user=request.user.id, up=True)
        v.save()
        tip_model.objects.filter(id=id).update(upvotes=F('upvotes')+1)
        return redirect("/")
    except Exception as e:
        return HttpResponse(e)

@login_required
def downvotes(request, id):
    try:
        if len(votes.objects.filter(id_content=id, id_user=request.user.id)) != 0:
            if votes.objects.filter(id_content=id, id_user=request.user.id, down=True):
                votes.objects.filter(id_content=id, id_user=request.user.id).delete()
                tip_model.objects.filter(id=id).update(downvotes=F('downvotes')-1)
            return redirect("/")
        v = votes(id_content=id, id_user=request.user.id, down=True)
        v.save()
        tip_model.objects.filter(id=id).update(downvotes=F('downvotes')+1)
        return redirect("/")
    except Exception as e:
        return HttpResponse(e)

@login_required
def delete(request, id):
    try:
        if len(votes.objects.filter(id_content=id, id_user=request.user.id)) != 0:
            votes.objects.filter(id_content=id, id_user=request.user.id).delete()
        tip_model.objects.filter(id=id).delete()
        return redirect("/")
    except Exception as e:
        return HttpResponse(e)

def logout(request):
    try:
        auth.logout(request)
        return redirect("/")
    except Exception as e:
        return HttpResponse(e)