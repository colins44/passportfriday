from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from .models import Route

class RouteResource(DjangoResource):
    # Controls what data is included in the serialized output.
    # preparer = FieldsPreparer(fields={
    #     'airport': 'airport.code',
    #     # 'inbound_flights': 'inbound_flights',
    # })

    def prepare(self, data):
        ret ={}
        for outbound_flight in data.outbound_flights.all():
            ret['departure_airport'] = outbound_flight.departure_airport.code
            ret['arrival_airport'] = outbound_flight.arrival_airport.code
        return ret



    # GET /
    def list(self):
        return Route.objects.all()

    # GET /pk/
    def detail(self, pk):
        return Route.objects.get(id=pk)

