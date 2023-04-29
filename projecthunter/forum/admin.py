from django.contrib import admin
from .models import *

@admin.register(Post)
class Post_Admin(admin.ModelAdmin):
	pass

class Post_Inline(admin.TabularInline):
	'''
	 Tabular Inline View for Post
	'''
	model = Post
	min_num = 3
	max_num = 20
	fk_name = 'theme'

@admin.register(Theme)
class Theme_Admin(admin.ModelAdmin):
	inlines = [Post_Inline]