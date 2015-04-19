from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from .models import  Flight, Slice
from datetime import datetime
from weekend.models import Dates
from flights.utils import process_qpx


class QPXResource(DjangoResource):

    def is_authenticated(self):
        # Open everything wide!
        # DANGEROUS, DO NOT DO IN PRODUCTION.
        return True

    # GET /
    def list(self):
        'return all slices'
        return 'this is a test'

    # PUT /api/route/<pk>/
    def update(self, pk):
        '''here we want to take in the PUT dict that contains the price data for the flights and save it
        this way we can have different QPS api keys getting flight prices
        get the data that is posted to this url and pass it along to the process_qpx function'''
        print self.data

    def create(self):
        print self.data
        # dates = Dates.objects.get(departure_date=self.data.get('dates').get('departure_date'))
        # process_qpx(self.data.get('qpx_data'), dates)




# class RouteResource(DjangoResource):
#     # Controls what data is included in the serialized output.
#     # preparer = FieldsPreparer(fields={
#     #     'airport': 'airport.code',
#     #     # 'inbound_flights': 'inbound_flights',
#     # })
#
#     def is_authenticated(self):
#         # Open everything wide!
#         # DANGEROUS, DO NOT DO IN PRODUCTION.
#         return True
#
#     def prepare(self, data):
#         ret ={}
#         ret['pk'] = data.pk
#         ret['weekend_destination'] = data.airport.iata
#         outbound_flights = []
#         inbound_flights = []
#         for flight in data.outbound_flights.all():
#             outbound_flight={}
#             outbound_flight['departure_airport'] = flight.departure_airport.iata
#             outbound_flight['departure_time'] = flight.departure_time
#             outbound_flight['carrier_code'] = flight.carrier_code
#             outbound_flight['arrival_airport'] = flight.arrival_airport.iata
#             outbound_flight['pk'] = flight.pk
#             outbound_flight['price'] = flight.price
#             outbound_flights.append(dict(outbound_flight))
#         for flight in data.inbound_flights.all():
#             inbound_flight={}
#             inbound_flight['departure_airport'] = flight.departure_airport.iata
#             inbound_flight['departure_time'] = flight.departure_time
#             inbound_flight['carrier_code'] = flight.carrier_code
#             inbound_flight['arrival_airport'] = flight.arrival_airport.iata
#             inbound_flights.append(dict(inbound_flight))
#         ret['outbound_flights'] = outbound_flights
#         ret['inbound_flights'] = inbound_flights
#         return ret
#
#     def create(self, data):
#         pass
#
#
#
#     # GET /
#     def list(self):
#         return Route.objects.all()[:5]
#
#     # GET /pk/
#     def detail(self, pk):
#         return Route.objects.get(id=pk)
#
#
#     # PUT /api/route/<pk>/
#     def update(self, pk):
#
#         for flight in self.data:
#             departure_date = datetime.strptime(flight['departure_date'], '%Y-%m-%d %H:%M')
#             fly = Flight.objects.get(carrier_code=flight['airline_code'],
#                                             departure_airport__iata=flight['departure_airport'],
#                                             arrival_airport__iata=flight['arrival_airport'],
#                                             departure_time=departure_date,)
#
#             fly.price = flight['price']
#             fly.save()




