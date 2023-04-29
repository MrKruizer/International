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
			HttpResponseRedirect('forum')
		else:
			return HttpResponseRedirect(reverse_lazy('login'))
	form = Post_Form()
	return render(request, 'create_post.html', context={'form': form})


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