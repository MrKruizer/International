from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^signup/$', views.signin, name='signup'),
    re_path(r'^signin/$', views.signup, name='signin'),
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^update_profile/$', views.update_profile, name='update_profile'),
    path('', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)