from django import forms
from django.forms import ModelForm, TextInput
from .models import Task

class MyForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ["title", "description"]
    widgets = {
      'title' : TextInput(attrs={
        'class' : 'form-control',
        'style': 'max-width: 300px;',
        'placeholder': 'title'
      }),
      'description' : TextInput(attrs={
        'class' : 'form-control',
        'style': 'max-width: 300px;',
        'placeholder': 'description'
      })
    }