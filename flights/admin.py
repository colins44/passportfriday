from django.contrib import admin
from .models import Flight, Airport, Slice, HistoricSlice

class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country')
    search_fields =('name',
                    'iata',
                    'country__name')

class FlightAdmin(admin.ModelAdmin):
    list_display =('departure_airport', 'arrival_airport')
    search_fields = ('departure_airport__name', 'arrival_airport__name', 'flight_no', 'carrier_code')
    list_filter = ('departure_time',)

class SliceAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination')
    search_fields = ('origin__name', 'destination__name')
    list_filter = ('price',)

class HistoricSliceAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination')
    search_fields = ('origin__name', 'destination__name')
    list_filter = ('price',)

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Slice, SliceAdmin)
admin.site.register(HistoricSlice, HistoricSliceAdmin)
