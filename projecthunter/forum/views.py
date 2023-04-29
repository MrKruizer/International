from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *
from hunter.models import Profile
import datetime

# Create your views here.
@login_required
def create_post(request, theme):
	if request.method == "POST":
		if request.user.is_authenticated:
			text = request.POST['text']
			user = request.user.id
			profile = Profile.objects.get(user_id = user)
			Post.objects.create(author = profile, theme_id=theme, text = text)
			return HttpResponseRedirect(reverse_lazy('posts', kwargs={'theme':theme.id}))
		else:
			return HttpResponseRedirect(reverse_lazy('login'))
	form = Post_Form()
	return render(request, 'create_post.html', context={'form': form})

@login_required
def update_post(request,theme,pk):
	if request.method == 'Post':
		text = request.POST['text']
		post = Post.objects.get(id = pk)
		post.text = text
		post.save(update_fields=['text'])
		return HttpResponseRedirect(reverse_lazy('posts', kwargs={'theme':theme.id}))
	form = Post_Form()
	return render(request, 'update_post.html', context={'form': form})

@login_required
def delete_theme(request,theme):
	if request.method == "Post":
		Post.objects.get

@login_required
def create_theme(request):
	if request.method == "POST":
		theme_name = request.POST['theme']
		text = request.POST['text']
		profile = Profile.objects.get(user_id = request.user.id)
		theme = Theme.objects.create(author = profile)
		post = Post.objects.create(author = profile, theme=theme, text = text)
		return HttpResponseRedirect(reverse_lazy('posts', kwargs={'theme':theme.id}))
	form = Forum_Form()
	return render(request, 'create_theme.html', context={'form': form})

@login_required
def update_theme(request, theme):
	if request.method == "POST":
		theme_name = request.POST['theme']
		theme_old = Theme.objects.get(id=theme)
		theme_old.theme = theme_name
		theme_old.save(update_fields=['theme'])
		return HttpResponseRedirect(reverse_lazy('posts', kwargs={'theme':theme.id}))
	form = Update_Forum_Form()
	return render(request, 'update_theme.html', context={'form':form})

class Posts_List_View(generic.ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'posts.html'
	paginate_by = 10
	redirect_field_name = 'next'
	def get_queryset(self):
		return Post.objects.filter(theme_id = self.kwargs['theme'])


class Forum_List_View(generic.ListView):
	model = Theme
	template_name = 'forum.html'
	context_object_name = 'Themes'
	paginate_by = 10
	redirect_field_name = 'next'