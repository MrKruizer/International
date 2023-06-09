from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','bio','avatar','skills', 'roles','phone', 'telegram']

class User_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
