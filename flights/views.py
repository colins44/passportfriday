from .models import Slice
from django.views.generic import ListView, DetailView, FormView, View
from datetime import datetime, timedelta
from .forms import ContactForm, NotificationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from email_user.forms import EmailUserCreationForm
from email_user.models import EmailUser
from django.contrib.auth.forms import UserCreationForm
from .forms import EmailSignUpForms



class Index(ListView):

    context_object_name = 'slices'
    queryset = Slice.objects.order_by('destination', 'price', 'dates').distinct('destination')
    # queryset = Slice.objects.values_list('destination', 'dates').distinct('destination', 'dates')
    template_name = "flights/home.html"
    paginate_by = 10


class Filter(ListView):

    #context_object_name = 'slices'
    template_name = 'flights/home.html'
    pageinate_by =10
    model = Slice

    def get_context_data(self, **kwargs):
        context = super(Filter, self).get_context_data(**kwargs)
        if 'price' in self.kwargs:
            print self.kwargs['price']
            context['title'] = 'filtered on price'
            context['slices'] = Slice.objects.order_by('dates', 'destination').distinct('dates', 'destination')

        if 'leavingDate' in self.kwargs:
            date_object = datetime.strptime(self.kwargs['leavingDate'], '%Y-%m-%d')
            next_day = date_object + timedelta(days=+1)
            print next_day
            context['title'] = 'filtered by weekend'
            context['slices'] = Slice.objects.filter(outbound_flights__departure_time__gt=date_object,
                                                     outbound_flights__departure_time__lt=next_day).order_by('outbound_flights__price')
        if 'city' in self.kwargs:
            context['routes'] = Slice.objects.filter(airport__city__name=self.kwargs['city'])
        return context


class Detail(DetailView):
    model = Slice
    template_name = "flights/detail.html"

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)


class Contact(FormView):
    template_name = 'flights/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(Contact, self).form_valid(form)

class Notifications(FormView):
    template_name = 'flights/notifications.html'
    form_class = NotificationForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(Notifications, self).form_valid(form)

class SignIn(FormView):
    form_class = AuthenticationForm
    template_name = 'flights/signin.html'

    def form_valid(self, form):
        redirect_to = settings.LOGIN_REDIRECT_URL
        login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return HttpResponseRedirect(redirect_to)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(SignIn, self).dispatch(request, *args, **kwargs)

class SignOut(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)


class SignUp(FormView):
    template_name = 'flights/signup.html'
    form_class = EmailUserCreationForm
    success_url='/account'

    def form_valid(self, form):
        #call the save function to save the new user
        form.save()
        # form.send_email()
        #get the username and password
        username = self.request.POST['email']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(SignUp, self).form_valid(form)







