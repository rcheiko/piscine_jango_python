from django import forms
from .models import Commentaire

class publishForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['message']