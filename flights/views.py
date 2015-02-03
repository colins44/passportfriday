from .models import  Route
from django.http import HttpResponse

def index(request):
    routes =  Route.objects.all()

    print a.parent_content_object.departure_airport
    print type(a)

    print round_trips.inbound_flights.all()

    return HttpResponse(a)

