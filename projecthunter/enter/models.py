from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

class Profile(models.Model):
	'''
	Model represent user profile
	'''
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	bio = models.TextField(max_length=1000, blank=True)
	skills = models.ManyToManyField(to='hunter.Skill')
	roles = models.ManyToManyField(to='hunter.Role')
	projects = models.ManyToManyField(to='hunter.Project', blank=True)
	avatar = models.ImageField(upload_to='static/images',height_field=None, width_field=None, max_length=100, default='static/image/profile.png')
	telegram = models.URLField(blank=True);
	phone = models.CharField(max_length=12,blank=True)
	def get_absolute_url(self):
		return reverse('profile', args=[str(self.id)])
	def __str__(self):
		return self.user.username

class User_Reputation(models.Model):
	source = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='source')
	target = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='target')

	def __str__(self):
		return f"{self.source.user.username} to {self.username.name}"
	
	
