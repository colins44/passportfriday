from django import forms
from .tasks import send_email
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField()
    email =forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        data = self.cleaned_data
        send_email.delay('flights/emails/thanks_for_getting_in_contact.html',
                        {'name': data['name'],
                         'subject': data['subject']},
                        [data['email'],],
                        "Thanks for getting in contact")
        send_email('flights/emails/new_message.html',
            {'from_name': data['name'],
             'from_address': data['email'],
             'subject': data['subject'],
             'message': data['message']}
                [settings.DEFAULT_TO_EMAIL],
            'A new contact form')


class NotificationForm(forms.Form):
    max_price = forms.IntegerField()
    email = forms.EmailField()
    name = forms.CharField(max_length=200)
    OPTIONS = (
                ("AUT", "Australia"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                )
    countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

    def send_email(self):
        data = self.cleaned_data
        send_email('flights/emails/set_up_notifications.html',
                   {'name': data['name'],
                    'max_price': data['max_price'],
                    'countries': data['countries']},
                    [data['email'],],
                    'You have set up a new Notification',)
