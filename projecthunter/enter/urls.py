from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^signin/$', views.signin, name='sigup'),
    re_path(r'^signup/$', views.signup, name='signin')
]