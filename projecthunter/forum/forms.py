from django import forms
from .models import *

class Forum_Form(forms.Form):
	theme = forms.CharField(max_length=254)
	text = forms.CharField(max_length=1000)

class Post_Form(forms.Form):
	text = forms.CharField(max_length=1000)

class Update_Forum_Form(forms.Form):
	theme = forms.CharField(max_length=254)