from django.conf.urls import patterns, include, url
from flights.views import Index, Detail, Contact, Filter, Notifications, SignIn, SignUp
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from flights.api import RouteResource
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^contact$', Contact.as_view(), name='contact'),
    url(r'^notifications$', Notifications.as_view(), name='notifications'),
    url(r'^(?P<pk>\d+)/$', Detail.as_view(), name='detail'),
    url(r'^price/(?P<price>\d+)/$', Filter.as_view(), name='filter'),
    url(r'^signin/$', SignIn.as_view(), name='signin'),
    url(r'^signup/$', SignUp.as_view(), name='signup'),
    url(r'^price/(?P<price>\d+)/$', Filter.as_view(), name='filter'),
    url(r'^leaving-date/(?P<leavingDate>[0-9\-_]+)/$', Filter.as_view()),
    url(r'^city/(?P<city>[A-z]+)/$', Filter.as_view()),
    url(r'^api/routes/', include(RouteResource.urls())),
    url(r'^thanks',TemplateView.as_view(template_name='flights/generic.html'),name='thanks'),
    url(r'^account',TemplateView.as_view(template_name='flights/generic.html'),name='thanks'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
