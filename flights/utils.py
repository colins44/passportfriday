from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.views.generic.base import TemplateResponseMixin
from django.template import loader, Context
import requests
import json
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from location.models import City
from flights.models import Airport, Flight
import datetime
from time import sleep

class TemplateEmailer(EmailMultiAlternatives, TemplateResponseMixin):

    def get_template_names(self, template):
        return template

    def __init__(self, template, context={}, **kwargs):
        t = loader.get_template(self.get_template_names(template))
        context.update({
            'email_from_name': settings.DEFAULT_FROM_NAME,
        })
        c = Context(context)
        self.rendered_message = t.render(c)
        if not kwargs.get('subject', None):
            kwargs['subject'] = settings.DEFAULT_FROM_NAME
        if not kwargs.get('from_email', None):
            kwargs['from_email'] = settings.DEFAULT_FROM_EMAIL

        super(TemplateEmailer, self).__init__(**kwargs)
        self.attach_alternative(self.rendered_message, "text/html")

    def send(self, fail_silently=False):
        """Just changes the default to fail_silently=True"""
        return super(TemplateEmailer, self).send(fail_silently)


def get_flight_data(airport, dates, hour):
        url = "https://api.flightstats.com/flex/schedules/rest/v1/json/from/%s/departing/%s/%s/%s/%d?appId=%s&appKey=%s" % (airport,
                                                                                                                            dates.departure_date.year,
                                                                                                                            dates.departure_date.month,
                                                                                                                            dates.departure_date.day,
                                                                                                                            hour,
                                                                                                                            settings.FLIGHTSTATS_APPID,
                                                                                                                            settings.FLIGHTSTATS_APPKEY)
        print url
        r = requests.get(url)
        outbound_flights = json.loads(r.content)
        sleep(2)

        for flight in outbound_flights['scheduledFlights']:
            if flight["isCodeshare"] is False:

                Airport.objects.get_or_create(iata=flight['departureAirportFsCode'])
                Airport.objects.get_or_create(iata=flight['arrivalAirportFsCode'])

                departure_date = datetime.datetime.strptime(flight['departureTime'], '%Y-%m-%dT%H:%M:%S.000')
                arrival_date = datetime.datetime.strptime(flight['arrivalTime'], '%Y-%m-%dT%H:%M:%S.000')
                departure_airport = Airport.objects.get(iata=flight['departureAirportFsCode'])
                arrival_airport = Airport.objects.get(iata=flight['arrivalAirportFsCode'])
                Flight.objects.create(departure_airport=departure_airport,
                                      arrival_airport=arrival_airport,
                                      departure_time=departure_date,
                                      flight_no= flight['flightNumber'],
                                      carrier_code= flight['carrierFsCode'],
                                      arrival_time= arrival_date,
                                      stops= flight['stops'],)

        for ap in outbound_flights['appendix']['airports']:
            try:
                city = City.objects.get(name__icontains=ap.get('city'), country__code=ap.get('countryCode'))
            except ObjectDoesNotExist:
                pass
            except MultipleObjectsReturned:
                pass
            else:
                city.code = ap.get('cityCode')
                city.save()

        url = "https://api.flightstats.com/flex/schedules/rest/v1/json/to/%s/arriving/%s/%s/%s/%d?appId=%s&appKey=%s" % (airport,
                                                                                                                        dates.departure_date.year,
                                                                                                                        dates.departure_date.month,
                                                                                                                        dates.departure_date.day,
                                                                                                                        hour,
                                                                                                                        settings.FLIGHTSTATS_APPID,
                                                                                                                        settings.FLIGHTSTATS_APPKEY)
        print url
        r = requests.get(url)
        inbound_flights = json.loads(r.content)
        sleep(2)

        for flight in inbound_flights['scheduledFlights']:
            if flight["isCodeshare"] is False:

                Airport.objects.get_or_create(iata=flight['departureAirportFsCode'])
                Airport.objects.get_or_create(iata=flight['arrivalAirportFsCode'])

                departure_date = datetime.datetime.strptime(flight['departureTime'], '%Y-%m-%dT%H:%M:%S.000')
                arrival_date = datetime.datetime.strptime(flight['arrivalTime'], '%Y-%m-%dT%H:%M:%S.000')
                departure_airport = Airport.objects.get(iata=flight['departureAirportFsCode'])
                arrival_airport = Airport.objects.get(iata=flight['arrivalAirportFsCode'])
                Flight.objects.create(departure_airport=departure_airport,
                                      arrival_airport=arrival_airport,
                                      departure_time=departure_date,
                                      flight_no= flight['flightNumber'],
                                      carrier_code= flight['carrierFsCode'],
                                      arrival_time= arrival_date,
                                      stops= flight['stops'],)

        for ap in inbound_flights['appendix']['airports']:
            try:
                city = City.objects.get(name__icontains=ap.get('city'), country__code=ap.get('countryCode'))
            except ObjectDoesNotExist:
                pass
            except MultipleObjectsReturned:
                pass
            else:
                city.code = ap.get('cityCode')
                city.save()