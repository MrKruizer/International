from django.contrib import admin
from .models import *

@admin.register(Tag)
class Tag_Admin(admin.ModelAdmin):
	pass

@admin.register(Role)
class Role_Admin(admin.ModelAdmin):
	pass

@admin.register(Skill)
class Skill_Admin(admin.ModelAdmin):
	pass
@admin.register(Project_Reputation)
class Project_Reputation_Admin(admin.ModelAdmin):
	pass
@admin.register(Project)
class Project_Admin(admin.ModelAdmin):
	pass
@admin.register(Team)
class Team_Admin(admin.ModelAdmin):
	pass