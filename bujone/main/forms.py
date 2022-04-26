from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import JournalModel
from .models import Todo



class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter todo', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))
    
    
        

class IdeaForm(forms.Form):
    text = forms.CharField(max_length=40,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter todo', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class JournalModelForm(forms.ModelForm):
    class Meta:
        model= JournalModel
        fields= ["title", "desc" , "user"]

