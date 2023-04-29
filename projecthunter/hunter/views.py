from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *

def project(request):
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
				tag = Tag.objects.get(name=self.request.GET['tag'])
				return Project.objects.filter(tag=tag)
		return Project.objects.all()

