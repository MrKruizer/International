from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User 
from django.urls import reverse_lazy
from django.views import generic
from  enter.models import Profile
from .models import *
from .forms import *

def project(request, pk):
	return render(request, 'catalog/project.html')



def project_create(request):

	profile = Profile.objects.get(user_id = request.user.id)
	if request.method=='POST':
		project = Project_Form(request.POST)
		profile = Profile.objects.get(user_id = request.user.id)
		project.author = profile.id
		project = project.save()
		last = Project.objects.filter(author = profile).last()
		profile.projects.add(last.id)
		profile.save()
		return HttpResponseRedirect(reverse_lazy('project', kwargs={'pk':project.id}))
	form = Project_Form(initial={'author': Profile})
	return render(request, 'catalog/project_create.html', context={'form': form})

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