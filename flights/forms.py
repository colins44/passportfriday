from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email =forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class NotificationForm(forms.Form):
    max_price = forms.IntegerField()
    email = forms.EmailField()
    OPTIONS = (
                ("AUT", "Australia"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                )
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass