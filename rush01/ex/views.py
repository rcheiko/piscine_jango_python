import json
from django.core.paginator import Paginator
from django.conf import Settings
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *
from .registerForm import register
from .loginForm import login
from django.contrib.auth.decorators import login_required
from .profileForm import profile
from django.db.models import Q
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import CreateView
from .publishForm import publishForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def profile_fct(request):
    if request.user.is_authenticated == False:
        return redirect("/")
    form = profile()
    u = User.objects.get(id=request.user.id)
    try:
        if (request.method == 'POST'):
            form = profile(request.POST, request.FILES)
            if form.is_valid():
                username = form.cleaned_data['username']
                surname = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                description = form.cleaned_data['description']
                profile_picture = form.cleaned_data['profile_picture']

                if len(username) >= 1:
                    u.username = username
                    u.save()

                if len(surname) >= 1:
                    u.last_name = surname
                    u.save()

                if len(email) >= 1:
                    u.email = email
                    u.save()

                if len(description) >= 1:
                    u.description = description
                    u.save()

                if type(profile_picture):
                    u.profile_picture = profile_picture
                    u.save()
                return redirect("/")
        else:
            form = profile()
    except Exception as e:
        print ('ERROR profile', e)
        return render(request, 'profile.html', {"form":form, "information":u})
    return render(request, "profile.html", {"form":form, "information":u})

def login_fct(request):
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


def register_fct(request):
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
        return render(request, 'register.html', {"form":form, "userExist":"Username Already Exist"})
    return render(request, 'register.html', {"form":form})

def logout(request):
    auth.logout(request)
    return redirect("/")

@login_required
def discussions(request):
    try:
        chats = Channel.objects.filter(Q(user_id1=request.user.id) | Q(user_id2=request.user.id))
    except Exception as error:
        return redirect(reverse("error"))
    chat_paginator = Paginator(chats, 10)
    page_num = request.GET.get('page')
    page = chat_paginator.get_page(page_num)
    usernames = []
    last_messages = []
    for chat in page:
        if chat.user_id1 == request.user.id:
            id = chat.user_id2
        else:
            id = chat.user_id1
        usernames.append(User.objects.get(id=id).username)
        msg = Message.objects.filter(channel_id=chat).last()
        if msg:
            s = str(msg)
            if len(s) > 30:
                s = s[0:30] + "..."
            last_messages.append({'msg': s, 'received': msg.received, 'date': msg.created})
        else:
            last_messages.append(None)
    return render(request, "discussions.html", {'page': page, 'usernames': usernames, 'last_messages': last_messages})

@login_required
def channel(request, id):
    try:
        user_id = request.user.id
        current_channel = Channel.objects.get(id=id)

        if user_id != current_channel.user_id1 and user_id != current_channel.user_id2:
            return redirect(reverse("home"))
        messages = Message.objects.filter(channel_id=id)
        for message in messages:
            if message.owner_id.id != user_id:
                message.received = True
                message.save()
    except Exception as error:
        return redirect(reverse("error"))
    return render(request, "channel.html", {'messages': messages, 'channel_id': id})

@login_required
def invite(request):
    if request.method == "POST":
        try:
            if 'invite' in request.POST:
                user_id1 = request.user.id
                user_id2 = User.objects.get(username=request.POST['invite']).id
                if user_id1 == user_id2:
                    return render(request, "invite.html", {'error': "Can't start chat with yourself"})
                Channel.objects.create(user_id1=user_id1, user_id2=user_id2)
        except Exception as error:
            return render(request, "invite.html", {'error': error})
    return render(request, "invite.html")

def error(request):
    return render(request, "error.html")

def profile_users(request):
    if request.user.is_authenticated == False:
        return redirect("/")
    users = User.objects.all().filter(~Q(id=request.user.id))
    return render(request, "profile_users.html", {'users': users})

def profile_user(request, id):
    if request.user.is_authenticated == False:
        return redirect("/")

    if request.method == "POST":
        if 'submit' in request.POST:
            id = request.user.id
            other_id = int(request.POST['submit'])
            try:
                channel = Channel.objects.get((Q(user_id2=other_id) | Q(user_id1=other_id)) & (Q(user_id1=id) | Q(user_id2=id)))
            except Channel.DoesNotExist:
                channel = None
            if not channel:
                try:
                    channel = Channel.objects.create(user_id1=id, user_id2=other_id)
                except Exception:
                    return render(request, "error.html")
            return redirect("/chat/" + str(channel.id))
    try:
        user = User.objects.get(id=id)
    except Exception as error:
        return render(request, "error.html")
    return render(request, "profile_user.html", {'user': user})

def add_admin_manually(request):
    if request.user.is_authenticated == False:
        return redirect("/")
    u = User.objects.get(id=request.user.id)
    u.is_staff = True
    u.save()
    return redirect("/")

@login_required
def staff(request):
    u = User.objects.get(id=request.user.id)
    if u.is_staff == False:
        return redirect("/")
    u = User.objects.all()
    context = {
        "user":u
    }
    return render(request, 'staff.html', context)

def add_admin_auto(request, id):
    u = User.objects.get(id=id)
    u.is_staff = True
    u.save()
    return redirect("/staff/")

def add_super_user_auto(request, id):
    u = User.objects.get(id=id)
    u.is_superuser = True
    u.save()
    return redirect("/staff/")

def delete_super_user_auto(request, id):
    u = User.objects.get(id=id)
    u.is_superuser = False
    u.save()
    return redirect("/staff/")

def delete_admin_auto(request, id):
    u = User.objects.get(id=id)
    u.is_staff = False
    u.save()
    return redirect("/staff/")

def forum(request):
    return render(request, "forum.html")

class ArticleList(ListView):
    model = Article
    template_name = "article_list.html"
    paginate_by = 10
    queryset = Article.objects.order_by('-created')

class ArticleDetails(DetailView):
    model = Article
    template_name = "article_details.html"
    def get(self, request, pk):
        if request.user.is_authenticated == False:
            return redirect("/")
        details = Article.objects.get(id=pk)
        All_Comments = Commentaire_post.objects.filter(article=details)
        return render(request, "article_details.html", {"details":details, "All_comments":All_Comments})

def comment_post(request):
    if request.method == 'POST':
        message = request.POST.get('commentaire')
        c_value = request.POST.get('c_value')
        article_id = request.POST.get('article_id')
        article_id = Article.objects.get(id=article_id)

        User_Object = request.user
        com = Commentaire_post.objects.get(id=c_value)
        register_post = Commentaire_post(
            author=User_Object,
            article=article_id,
            comment=com,
            message=message,
        )
        register_post.save()

        data = json.dumps({})

        return HttpResponse(data, content_type="application/json")
    else:
        raise Http404

def comment_post_first(request):
    if request.method == 'POST':
        message = request.POST.get('commentaire')
        article_id = request.POST.get('article_id')
        article_id = Article.objects.get(id=article_id)

        User_Object = request.user
        register_post = Commentaire_post(
            author=User_Object,
            article=article_id,
            message=message,
        )
        register_post.save()

        data = json.dumps({
        })
        return HttpResponse(data, content_type="application/json")

    else:
        raise Http404

class publish_article(CreateView):
    model = Article
    form_class = publishForm
    template_name = "publish_article.html"

    def get(self, request):
        return render(request, 'publish_article.html', {"form":self.form_class})

    def post(self, request):
        if (request.method == 'POST'):
            try:
                form_publish = publishForm(request.POST)
                if form_publish.is_valid():
                    form_publish = Article(
                        title=form_publish.cleaned_data['title'],
                        content=form_publish.cleaned_data['content'],
                        author=request.user,
                    )
                    form_publish.save()
                    form_publish = publishForm()
                    return redirect("/article_list")
            except Exception as e:
                form_publish = publishForm()
                return render(request, 'publish_article.html', {"form":form_publish})
        return render(request, 'publish_article.html', {"form":form_publish})
