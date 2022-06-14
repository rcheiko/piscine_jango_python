from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from ex00.loginForm import login
from ex00.models import *

# Create your views here.

class publication_list(ListView):
    model = Article
    template_name = "publication_list.html"

class publication_detail(DetailView):
    model = Article
    template_name = "publication_detail.html"
    def get(self, request, pk):
        details = Article.objects.get(id=pk)
        return render(request, "publication_detail.html", {"details":details})

    def post(self, request, pk):
        if (request.method == 'POST'):
            try:
                User_Object = request.user
                details = Article.objects.get(id=pk)
                Favorite = UserFavouriteArticle(
                    user=User_Object,
                    article=details
                )
                Favorite.save()
                return redirect("/favourite_article")
            except Exception as e:
                return render(request, "publication_detail.html", {"details":details})

class logout_class(ListView):
    def get(self, request):
        auth.logout(request)
        return redirect("/")


class favourite_article(ListView):
    model = UserFavouriteArticle
    template_name = "favourite_article.html"