from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Forum_List_View.as_view(), name='forum'),
    re_path(r'^theme/(?P<theme>\d+)/$', views.Posts_List_View.as_view(), name='posts'),
    re_path(r'^theme/(?P<theme>\d+)/create/$', views.create_post, name='create_post'),
    re_path(r'^theme/(?P<theme>\d+)/(?P<pk>\d+)/update/$', views.update_post, name='update_post'),
    re_path(r'^theme/create/$', views.create_theme, name='create_theme'),
    re_path(r'^theme/(?P<theme>\d+)/update/$', views.update_theme, name='update_theme'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)