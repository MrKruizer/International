from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User 
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *

def project(request, pk):
	return render(request, 'catalog/project.html')




class Project_List_View(generic.ListView):
	model = Project
	context_object_name = 'project_list'
	template_name = "catalog/catalog.html"
	paginate_by = 10
	redirect_field_name = 'next'
	def get_queryset(self):
		if self.request.method == 'GET':
			if 'tag' in self.request.GET.keys():
				try:
					tag = Tag.objects.get(name=self.request.GET['tag'])
				except:
					return Project.objects.all()
				return Project.objects.filter(tags=tag)
		return Project.objects.all()