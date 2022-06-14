from django import forms
from .models import User

class profile(forms.ModelForm):
    username = forms.CharField(max_length=20 ,required=False)
    last_name = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(max_length=40, required=False)
    description = forms.CharField(max_length=128 ,required=False)
    profile_picture = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'description', 'profile_picture']
