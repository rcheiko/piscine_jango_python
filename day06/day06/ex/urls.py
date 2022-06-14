from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_fct),
    path('register/', views.register_fct),
    path('logout/', views.logout),
    path('upvotes/<int:id>', views.upvotes, name="upvotes"),
    path('downvotes/<int:id>', views.downvotes, name="downvotes"),
    path('delete/<int:id>', views.delete, name="delete"),
]