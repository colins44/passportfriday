from django.contrib import admin
from .models import Flight, Airport, Route


class FlightAdmin(admin.ModelAdmin):
    list_display =('departure_airport', 'arrival_airport')
    search_fields = ('departure_airport', 'arrival_airport')
    list_filter = ('departure_time',)


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Airport)
admin.site.register(Route)
admin.site.register(Flight, FlightAdmin)
