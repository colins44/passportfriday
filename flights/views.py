from .models import RoundTrip
from django.http import HttpResponse

def index(request):
    round_trips = RoundTrip.objects.get(id=1)
    a = round_trips.inbound_flights.all()[0]
    print a.parent_content_object.departure_airport
    print type(a)

    print round_trips.inbound_flights.all()

    return HttpResponse(a)

