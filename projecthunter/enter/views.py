from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def signup(request):
	if request.method == "POST":
		user = User_Form(request.POST)
		user.save()
		username=request.POST.get('username')
		uuser = User.objects.get(username=username)
		profile = Profile(user_id = uuser.id, bio=request.POST['bio'],avatar=request.POST['avatar'])
		profile.save()
		profile.skills.set(request.POST['skills'])
		profile.roles.set((request.POST['roles']))
		profile.save()
		return HttpResponseRedirect(reverse_lazy('signin'))
	form_u = User_Form()
	form_p = Profile_Form()
	return render(request, 'signup.html', context={'form_u': form_u, 'form_p':form_p})

def profile(request, pk):
	return render(request, 'profile.html', context={'profile': Profile.objects.get(id=pk)})

class Profile_Update_View(UpdateView):
    model = Profile
    template_name = "update_profile.html"
    fields = ['avatar', 'bio', 'skills','roles','telegram','phone']
