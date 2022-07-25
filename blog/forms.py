from django import forms
from django.db import models


class PostFormulario(forms.Form):
    titulo=forms.CharField(max_length=50)
    contenido=forms.CharField(max_length=5000)
    imagen=forms.ImageField(required=False)
    #autor=forms.ForeignKey(User, on_delete=models.CASCADE)
    #autor=models.ForeignKey(User, on_delete=models.CASCADE) # revisar si el ultimo es models o forms.CASACADE
    