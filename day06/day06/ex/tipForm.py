from django import forms
import datetime
from django.contrib import auth
from .models import tip_model

# Create your models here.

class tip_form(forms.ModelForm):
    class Meta:
        model = tip_model
        fields = ['content', 'author', 'date']