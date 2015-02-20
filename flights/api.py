from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from .models import Route

class RouteResource(DjangoResource):
    # Controls what data is included in the serialized output.
    # preparer = FieldsPreparer(fields={
    #     'airport': 'airport.code',
    #     # 'inbound_flights': 'inbound_flights',
    # })

    def is_authenticated(self):
        # Open everything wide!
        # DANGEROUS, DO NOT DO IN PRODUCTION.
        return True

    def prepare(self, data):
        ret ={}
        ret['pk'] = data.pk
        ret['weekend_destination'] = data.airport.code
        ret['price'] = data.price
        outbound_flight = {}
        inbound_flight = {}
        for flight in data.outbound_flights.all():
            outbound_flight['departure_airport'] = flight.departure_airport.code
            outbound_flight['departure_time'] = flight.departure_time
            outbound_flight['carrier_code'] = flight.carrier_code
            outbound_flight['arrival_airport'] = flight.arrival_airport.code
        for flight in data.inbound_flights.all():
            inbound_flight['departure_airport'] = flight.departure_airport.code
            inbound_flight['departure_time'] = flight.departure_time
            inbound_flight['carrier_code'] = flight.carrier_code
            inbound_flight['arrival_airport'] = flight.arrival_airport.code
        ret['outbound_flight'] = outbound_flight
        ret['inbound_flight'] = inbound_flight
        return ret



    # GET /
    def list(self):
        return Route.objects.all()

    # GET /pk/
    def detail(self, pk):
        return Route.objects.get(id=pk)

    # Add this!
    # PUT /api/route/<pk>/
    def update(self, pk):
        self.data['price'].decode('utf8')
        route = Route.objects.get(id=pk)
        route.price = self.data['price']
        route.save()
        return route



