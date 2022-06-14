from django import forms
import datetime
from django.contrib import auth
from ex00.models import Article
from django.contrib.auth.models import User

class publish(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']