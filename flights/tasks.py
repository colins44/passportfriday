from flightdata import inbound_flights, outbound_flights
from flights.models import Flight

for flight in inbound_flights['scheduledFlights']:
    print flight['arrivalAirportFsCode'], flight ['departureAirportFsCode']
    Flight.objects.create(departure_airport=flight ['departureAirportFsCode'], arrival_airport=flight['arrivalAirportFsCode'])

for flight in outbound_flights['scheduledFlights']:
    print flight['arrivalAirportFsCode'], flight ['departureAirportFsCode']
    inbound_flights_to_this_airport = Flight.objects.filter(arrival_airport=flight['departureAirportFsCode'])
    Flight.objects.create(departure_airport=flight ['departureAirportFsCode'], arrival_airport=flight['arrivalAirportFsCode'])

all_flights = Flight.objects.all()

