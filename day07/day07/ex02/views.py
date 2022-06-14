from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from ex00.loginForm import login
from ex00.models import *
from .publishForm import publish
from .registerForm import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

# Create your views here.

class register_class(CreateView):
    model = User
    form_class = CustomUserCreationForm
    # fields = ['username', 'password1', 'password2']
    template_name = "register.html"
    success_url="/"

class publish_class(CreateView):
    model = Article
    form_class = publish
    template_name = "publish.html"

    def get(self, request):
        if request.user.is_authenticated == False:
            return redirect("/")
        return render(request, 'publish.html', {"form":self.form_class})

    def post(self, request):
        if (request.method == 'POST'):
            try:
                form_publish = publish(request.POST)
                if form_publish.is_valid():
                    form_publish = Article(
                        title=form_publish.cleaned_data['title'],
                        synopsis=form_publish.cleaned_data['synopsis'],
                        content=form_publish.cleaned_data['content'],
                        author=request.user,
                    )
                    form_publish.save()
                    form_publish = publish()
                    return render(request, 'publish.html', {"form":form_publish})
            except Exception as e:
                form_publish = publish()
                print('erreurrrrrrrrrrrrrrrrrrrrrr', e)
                return render(request, 'publish.html', {"form":form_publish})
        return render(request, 'publish.html', {"form":form_publish})