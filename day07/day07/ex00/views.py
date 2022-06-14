from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, FormView
from .loginForm import login
from .models import *

# Create your views here.


class home(ListView):
    def get(self, request):
        return redirect("/article")

class login_class(FormView):
    template_name="login.html"
    form_class=login

    def get(self, request):
        f = login()
        return render(request, 'login.html', {"form":f})

    def post(self, request):
        if (request.method == 'POST'):
            f = login(request.POST)
            if f.is_valid():
                username = f.cleaned_data['username']
                password = f.cleaned_data['password']
                user = auth.authenticate(username=username,
                                         password=password)
                if user and user.is_active:
                    auth.login(request, user)
                    return redirect("/")
                else:
                    f._errors['username'] = ['This user doesn\'t exist.']

        return render(request, 'login.html', {"form":f})

class populate(ListView):
    def get(self, request):
        try:
            u1 = User.objects.create_user('shokker', None, '1')
            u2 = User.objects.create_user('q', None, '2')
            u3 = User.objects.create_user('Pierre', None, '3')

            m1 = Article(
                    title="The Phantom Menace",
                    author=u1,
                    synopsis="Rick McCallum",
                    content="George Lucas"
            )
            m1.save()

            m2 = Article(
                    title="Attack of the Clones",
                    author=u2,
                    synopsis="Rick McCallum",
                    content="George Lucas"
            )
            m2.save()

            m3 = Article(
                    title="Revenge of the Sith",
                    author=u3,
                    synopsis="Rick McCallum",
                    content="George Lucas"
            )
            m3.save()

            m4 = Article(
                    title="A New Hope",
                    author=u1,
                    synopsis="Gary Kurtz, Rick McCallum",
                    content="1977-05-25"
            )
            m4.save()

            m5 = Article(
                    title="Iron man et les 5 nains",
                    author=u1,
                    synopsis="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut congue, dui quis feugiat cursus, risus enim faucibus diam, vel sollicitudin ipsum erat at purus.",
                    content="Contenu non explicite"
            )
            m5.save()

            User_Object = User.objects.get(id=1)
            print(User_Object)
            Article_1 = Article.objects.get(id=1)
            print(Article_1)
            Article_2 = Article.objects.get(id=2)
            print(Article_2)

            Favorite1 = UserFavouriteArticle(
                user=User_Object,
                article=Article_1
            )
            Favorite1.save()

            Favorite2 = UserFavouriteArticle(
                user=User_Object,
                article=Article_2
            )
            Favorite2.save()

        except Exception as e:
            return HttpResponse(e)
        return HttpResponse("OK")

class ArticleList(ListView):
    model = Article
    template_name = "article.html"