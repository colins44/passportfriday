from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from .models import Route, Flight
from datetime import datetime

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
        ret['weekend_destination'] = data.airport.iata
        outbound_flights = []
        inbound_flights = []
        for flight in data.outbound_flights.all():
            outbound_flight={}
            outbound_flight['departure_airport'] = flight.departure_airport.iata
            outbound_flight['departure_time'] = flight.departure_time
            outbound_flight['carrier_code'] = flight.carrier_code
            outbound_flight['arrival_airport'] = flight.arrival_airport.iata
            outbound_flight['pk'] = flight.pk
            outbound_flight['price'] = flight.price
            outbound_flights.append(dict(outbound_flight))
        for flight in data.inbound_flights.all():
            inbound_flight={}
            inbound_flight['departure_airport'] = flight.departure_airport.iata
            inbound_flight['departure_time'] = flight.departure_time
            inbound_flight['carrier_code'] = flight.carrier_code
            inbound_flight['arrival_airport'] = flight.arrival_airport.iata
            inbound_flights.append(dict(inbound_flight))
        ret['outbound_flights'] = outbound_flights
        ret['inbound_flights'] = inbound_flights
        return ret

    def create(self, data):
        pass



    # GET /
    def list(self):
        return Route.objects.all()[:5]

    # GET /pk/
    def detail(self, pk):
        return Route.objects.get(id=pk)


    # PUT /api/route/<pk>/
    def update(self, pk):

        for flight in self.data:
            departure_date = datetime.strptime(flight['departure_date'], '%Y-%m-%d %H:%M')
            fly = Flight.objects.get(carrier_code=flight['airline_code'],
                                            departure_airport__iata=flight['departure_airport'],
                                            arrival_airport__iata=flight['arrival_airport'],
                                            departure_time=departure_date,)

            fly.price = flight['price']
            fly.save()




