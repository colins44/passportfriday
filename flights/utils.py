from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.views.generic.base import TemplateResponseMixin
from django.template import loader, Context

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
