from django.contrib import admin
from .models import InboundFlights, OutboundFlights, Flight, RoundTrip, Airport, Route
from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline

class OutboundFlightsInline(GenericTabularInline):
    model = InboundFlights
    fields = ['parent_content_type','parent_object_id']
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 0

class InboundFlightsInline(GenericTabularInline):
    model = OutboundFlights
    fields = ['parent_content_type','parent_object_id',]
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 0

class RoundTripAdmin(GenericAdminModelAdmin):
    inlines = [OutboundFlightsInline,InboundFlightsInline]

admin.site.register(RoundTrip, RoundTripAdmin)
admin.site.register(Airport)
admin.site.register(Route)
admin.site.register(Flight)
