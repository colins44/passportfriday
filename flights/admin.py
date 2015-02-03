from django.contrib import admin
from .models import Flight, Airport, Route



admin.site.register(Airport)
admin.site.register(Route)
admin.site.register(Flight)
