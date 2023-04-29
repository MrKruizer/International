from django.contrib import admin
from .models import *

@admin.register(Profile)
class Profile_Admin(admin.ModelAdmin):
	pass
@admin.register(User_Reputation)
class User_Reputation_Admin(admin.ModelAdmin):
	pass
