from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)