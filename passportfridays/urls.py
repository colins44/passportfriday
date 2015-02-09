from django.conf.urls import patterns, include, url
from flights.views import Index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from flights.api import RouteResource
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'passportfridays.views.home', name='home'),
    # url(r'^passportfridays/', include('passportfridays.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', views.index, name='index'),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^api/routes/', include(RouteResource.urls())),
)
