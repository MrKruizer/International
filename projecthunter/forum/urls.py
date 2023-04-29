from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Forum_List_View.as_view(), name='forum'),
    re_path(r'^theme/?P<theme>\d+/$', views.Posts_List_View.as_view, name='posts'),
    re_path(r'^theme/?P<theme>\d+/create$', views.create_post, name='create_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)