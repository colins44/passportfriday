from django.contrib import admin
from .models import Flight, Airport, Slice

class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country')
    search_fields =('name', 'iata')

class FlightAdmin(admin.ModelAdmin):
    list_display =('departure_airport', 'arrival_airport')
    search_fields = ('departure_airport__name', 'arrival_airport__name', 'flight_no', 'carrier_code')
    list_filter = ('departure_time',)

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Slice)
