from django.conf.urls import patterns, include, url
from flights.views import Index, Detail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from flights.api import RouteResource
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', Detail.as_view(), name='detail'),
    (r'^price/(?P<price>\d+)/$', Index.as_view()),
    url(r'^api/routes/', include(RouteResource.urls())),

)
