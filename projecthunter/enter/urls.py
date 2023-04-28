from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^signin/$', views.signin, name='sigup'),
    re_path(r'^signup/$', views.signup, name='signin')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)