from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.allClubs),
    url(r'^club/(?P<num>\d+)$', views.display_club),
    url(r'^request/(?P<num>\d+)$', views.display_request),
    url(r'^lookup/$', views.display_search),
    url(r'^getChart/$', views.populateChart),

)

