from django.utils.translation import gettext_lazy as gtl
from django.core.exceptions import ValidationError
from django import forms
from .models import *
import datetime

class Forum_Form(forms.Form):
	theme = forms.CharField(max_length=254)
	text = forms.CharField(max_length=1000)

class Post_Form(forms.Form):
	text = forms.CharField(max_length=1000)