from django import forms
from .models import *

class Project_Form(forms.ModelForm):
	class meta:
		model = Project
		fields = ['name', 'description','skills', 'roles', 'tags']
	name = forms.CharField(max_length=254)
	description = forms.CharField(max_length=1000)
	skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)
	tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
	roles = forms.ModelMultipleChoiceField(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple)