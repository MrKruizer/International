from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.Project_List_View.as_view(), name='catalog'),
    re_path(r'^project/', views.project, name='project'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
