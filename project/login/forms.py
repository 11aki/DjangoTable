from typing import OrderedDict
import django
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Movie

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'



