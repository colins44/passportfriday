from django.contrib import admin
from .models import Flight, Airport, Route, Slice

class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country')
    search_fields =('name', 'iata')

class FlightAdmin(admin.ModelAdmin):
    list_display =('departure_airport', 'arrival_airport')
    search_fields = ('departure_airport__name', 'arrival_airport__name', 'flight_no', 'carrier_code')
    list_filter = ('departure_time',)


class RouteAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'departure_date', 'return_date')
    search_fields = ('origin',)
    readonly_fields = ('outbound_flights', 'inbound_flights',)


admin.site.register(Airport, AirportAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Slice)
