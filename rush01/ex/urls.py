from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name="home"),
    #USER
    path('login/', views.login_fct, name="login"),
    path('register/', views.register_fct, name="register"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile_fct, name="profile"),
    path('profile_user/', views.profile_users, name="profile_users"),
    path('profile_user/<int:id>', views.profile_user, name="profile_user"),

    #CHAT
    path('discussions/', views.discussions, name="discussions"),
    path('chat/<int:id>', views.channel, name="channel"),
    path('invite/', views.invite, name="invite"),

    ## ADMIN
    path('add_admin_manually/', views.add_admin_manually),
    path('staff/', views.staff),
    path('add_admin_auto/<int:id>', views.add_admin_auto, name="add"),
    path('add_super_user_auto/<int:id>', views.add_super_user_auto, name="add_super"),
    path('delete_admin_auto/<int:id>', views.delete_admin_auto, name="delete"),
    path('delete_super_user_auto/<int:id>', views.delete_super_user_auto, name="delete_super"),

    ##FORUM
    path('forum/', views.forum),
    path('comment_post/', views.comment_post),
    path('comment_post_first/', views.comment_post_first),

    path('article_list/', login_required(views.ArticleList.as_view())),
    re_path(r'article_details/(?P<pk>[0-9]+)', login_required(views.ArticleDetails.as_view()), name="article_details"),
    path('publish_article/', login_required(views.publish_article.as_view())),

    #ERROR
    path('error/', views.error, name="error"),
]