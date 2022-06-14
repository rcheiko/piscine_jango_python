from django.urls import path
from . import views
from ex01 import views as viewsex01
from ex02 import views as viewsex02

urlpatterns = [
    path('', views.home.as_view()),
    path('login/', views.login_class.as_view(), name='login'),
    path('register/', viewsex02.register_class.as_view()),
    path('logout/', viewsex01.logout_class.as_view()),
    path('populate/', views.populate.as_view()),
    path('article/', views.ArticleList.as_view()),
    path('publication_list/', viewsex01.publication_list.as_view()),
    path('publication_detail/(?P<pk>[0-9]+)', viewsex01.publication_detail.as_view(), name="publication_detail"),
    path('favourite_article/', viewsex01.favourite_article.as_view()),
    path('publish/', viewsex02.publish_class.as_view()),
]