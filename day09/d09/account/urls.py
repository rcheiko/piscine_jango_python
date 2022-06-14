from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('ajax/login_request', views.login_request),
    path('logout', views.logout),
]