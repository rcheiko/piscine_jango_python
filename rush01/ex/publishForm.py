from django import forms
from .models import Article

class publishForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']