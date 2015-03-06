from django.conf.urls import patterns, include, url
from flights.views import Index, Detail, Contact, Filter
from django.conf import settings
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from flights.api import RouteResource
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^contact$', Contact.as_view(), name='contact'),
    url(r'^(?P<pk>\d+)/$', Detail.as_view(), name='detail'),
    url(r'^price/(?P<price>\d+)/$', Filter.as_view(), name='filter'),
    url(r'^leaving-date/(?P<leavingDate>[0-9A-z\-_]+)/$', Filter.as_view()),
    url(r'^api/routes/', include(RouteResource.urls())),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
