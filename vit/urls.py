from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.static import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('vit.art.views',
    # url(r'^$', 'vit.views.home', name='home'),
    # url(r'^vit/', include('vit.foo.urls')),
    (r"^(\d+)/$", 'post'),
    (r'^main/$', 'main'),
#    (r'^post/$', 'post'),
    (r'^index/$', 'index'),
#    (r"", "main"),
     url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
