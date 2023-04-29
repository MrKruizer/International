from django.db import models
from enter.models import *
from forum.models import *
import uuid

class Tag(models.Model):
	"""
	Model representing a project tag (e.g. ML, Web etc).
	"""
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Skill(models.Model):
	"""
	Model representing a needed skill and user skill
	"""
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Role(models.Model):
	"""
	Model representing the necessary and preferred role
	"""
	name = models.CharField(max_length=200)
	grades = (('j','Junior'), ('m','Middle'), ('s' , 'Senior'), ('l', "Team lead"))
	grade = models.CharField('Grade', max_length=1, choices=grades, default='j')
	unique_together = (('name','grade'),)
	def __str__(self):
		return f'{self.name} {self.grade}'


class Project_Reputation(models.Model):
	source = models.ForeignKey('enter.Profile', on_delete=models.CASCADE)
	project = models.ForeignKey('Project', on_delete=models.CASCADE)

class Project(models.Model):
	"""
	Model representing the project
	"""
	name = models.CharField(max_length=254)
	logo = models.ImageField(upload_to='static/images',height_field=None, width_field=None, max_length=100, default='static/image/cv.png')
	tags = models.ManyToManyField(Tag,blank=True)
	skills = models.ManyToManyField(Skill, blank=True)
	description = models.TextField(blank=True, max_length=1000)
	git = models.URLField(max_length = 254, blank=True)
	uurl = models.UUIDField('Invite ref',default=uuid.uuid4,help_text='Unique identifier for the referral invitation to the team')
	def __str__(self):
		return self.name
	def get_author_username(self):
		return Profile.objects.get(projects=self.id).user.username
	def reputation(self):
		return len(Project_Reputation.objects.filter(project=self.id))
	
class Team(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE)
	role = models.ForeignKey('Role', on_delete=models.CASCADE)
	profile = models.ForeignKey('enter.Profile', on_delete=models.CASCADE)

	def __str__(self):
		return f'teams {self.project.name}'