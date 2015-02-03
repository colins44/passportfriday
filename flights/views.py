from .models import  Route
from django.http import HttpResponse
from django.views.generic import ListView

class Index(ListView):

    context_object_name = 'routes'
    queryset = Route.objects.all()
    template_name = "flights/home.html"

# def index(request):
#     routes =  Route.objects.all()
#     round_trips = RoundTrip.objects.get(id=1)
#     a = round_trips.inbound_flights.all()[0]
#     print a.parent_content_object.departure_airport
#     print type(a)
#
#     print round_trips.inbound_flights.all()
#
#     return HttpResponse(a)

