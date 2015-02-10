from .models import  Route
from django.http import HttpResponse
from django.views.generic import ListView

class Index(ListView):

    context_object_name = 'routes'
    queryset = Route.objects.all()
    template_name = "flights/home.html"



