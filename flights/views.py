from .models import  Route
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from flights.utils import SortMixin, FilterMixin

class Index(ListView, SortMixin, FilterMixin):

    context_object_name = 'routes'
    queryset = Route.objects.all()
    template_name = "flights/home.html"
    paginate_by = 2
    # model = Route.objects.all()

    # def get_queryset(self):
    #     return Route.objects.all().order_by('-price')
    #
    # def get_context_data(self, **kwargs):
    #     context = super(Index, self).get_context_data(**kwargs)
    #     if self.kwargs:
    #         context['title'] = 'filtered on price'
    #         context['routes'] = Route.objects.filter(price__lte=self.kwargs['price'])
    #     else:
    #         context['title'] = 'home'
    #         context['routes'] = Route.objects.all()[:20]
    #
    #     return context



class Detail(DetailView):
    model = Route
    template_name = "flights/detail.html"

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        print "$$$$$$$"
        print context
        print kwargs
        return context

class Contact(TemplateView):

    template_name = 'flights/index.html'

