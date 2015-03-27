from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.allClubs),
    url(r'^club/(?P<num>\d+)$', views.display_club),
    url(r'^stat/$', views.returnStat),

)

