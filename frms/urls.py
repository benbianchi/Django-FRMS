from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('archive.urls')),
    url(r'^admin/dashboard/', include(admin.site.urls)),
)