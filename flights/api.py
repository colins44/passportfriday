from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from .models import Slice
from datetime import datetime
from weekend.models import Dates
from flights.utils import process_qpx
from django.conf.urls import patterns, url


class QPXResource(DjangoResource):

    def is_authenticated(self):
        # Open everything wide!
        # DANGEROUS, DO NOT DO IN PRODUCTION.
        return True

    def create(self):
        departure_date = datetime.strptime(self.data.get('dates').get('departure_date'), '%Y-%m-%d')
        return_date = datetime.strptime(self.data.get('dates').get('return_date'), '%Y-%m-%d')
        dates = Dates.objects.get(departure_date=departure_date, return_date=return_date)
        return process_qpx(self.data.get('qpx_data'), dates)

class SliceResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'origin': 'origin.name',
        'destination': 'destination.name',
        'price': 'price',
        'currency': 'currency.code',
        'quote_time': 'quote_time',
        'outbound_flight_number':'outbound_flight.flight_no',
        'outbound_flight_code':'outbound_flight.carrier_code',
        'inbound_flight_number':'inbound_flight.flight_no',
        'inbound_flight_code':'inbound_flight.carrier_code',
    })

    def list(self, *args, **kwargs):
        return Slice.objects.all().order_by('price')

    def detail(self, pk):
        return Slice.objects.get(id=pk)


    @classmethod
    def urls(cls, name_prefix=None):
        return patterns('',
            url(r'^$', cls.as_view('list'), name='list_slices'),
            url(r'^(?P<pk>\d+)/$', cls.as_detail('detail'), name='detail_slice'),
        )



