from .models import Route
from django.views.generic import ListView, DetailView, FormView
from flights.utils import SortMixin, FilterMixin
from datetime import datetime, timedelta
from .forms import ContactForm, NotificationForm
from django.contrib.auth.forms import AuthenticationForm

class Index(ListView, SortMixin, FilterMixin):

    context_object_name = 'routes'
    queryset = Route.objects.all().order_by('outbound_flights__price')[:10]
    template_name = "flights/home.html"
    paginate_by = 2


class Filter(ListView):

    # context_object_name = 'routes'
    template_name = 'flights/home.html'
    pageinate_by =10
    model = Route

    def get_context_data(self, **kwargs):
        context = super(Filter, self).get_context_data(**kwargs)
        if 'price' in self.kwargs:
            print self.kwargs['price']
            context['title'] = 'filtered on price'
            context['routes'] = Route.objects.filter(outbound_flights__price__lte=self.kwargs['price']).order_by('outbound_flights__price')
            print context['routes']

        if 'leavingDate' in self.kwargs:
            date_object = datetime.strptime(self.kwargs['leavingDate'], '%Y-%m-%d')
            next_day = date_object + timedelta(days=+1)
            print next_day
            # context['title'] = 'filtered by weekend'
            context['routes'] = Route.objects.filter(outbound_flights__departure_time__gt=date_object,
                                                     outbound_flights__departure_time__lt=next_day).order_by('outbound_flights__price')
        if 'city' in self.kwargs:
            context['routes'] = Route.objects.filter(airport__code=self.kwargs['city'])
        return context


class Detail(DetailView):
    model = Route
    template_name = "flights/detail.html"

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)


class Contact(FormView):
    template_name = 'flights/elements.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(Contact, self).form_valid(form)

class Notifications(FormView):
    template_name = 'flights/notifications.html'
    form_class = NotificationForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(Notifications, self).form_valid(form)



