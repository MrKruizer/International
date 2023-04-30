from enter.models import Profile
from django import forms
from .models import *

class Project_Form(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'description','skills', 'roles', 'tags', 'author']
	name = forms.CharField(max_length=254)
	description = forms.CharField(max_length=1000)
	skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)
	tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
	roles = forms.ModelMultipleChoiceField(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple)
	author = forms.ModelChoiceField(queryset=Profile.objects.all())