from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile'),
    re_path(r'^profile/(?P<pk>\d+)/update/$', views.Profile_Update_View.as_view(), name='update_profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)