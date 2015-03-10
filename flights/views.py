from .models import Route
from django.views.generic import ListView, DetailView, FormView, View
from datetime import datetime, timedelta
from .forms import ContactForm, NotificationForm, UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib.auth import authenticate, login


class Index(ListView):

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
        auth_login(self.request, form.get_user())
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
        auth_logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

class SignUp(FormView):
    template_name = 'flights/signup.html'
    form_class = UserCreateForm
    success_url='/account'

    def form_valid(self, form):
        #call the save function to save the new user
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(SignUp, self).form_valid(form)



#http://stackoverflow.com/questions/3222549/how-to-automatically-login-a-user-after-registration-in-django
#http://stackoverflow.com/a/28974691/2319915
#http://stackoverflow.com/questions/6034763/django-attributeerror-user-object-has-no-attribute-backend-but-it-does




