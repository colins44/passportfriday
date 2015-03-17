""" User models."""
import hashlib
import random
# import re
# import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.contrib.sites.models import Site, RequestSite
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from flights.tasks import send_email
# from django.db.models.deletion import Collector
# from django.db import (router, transaction, DatabaseError,
#     DEFAULT_DB_ALIAS)


class EmailUserManager(BaseUserManager):

    """ Custom manager for EmailUser."""

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """ Create and save an EmailUser with the given email and password.

        :param str email: user email
        :param str password: user password
        :param bool is_staff: whether user staff or not
        :param bool is_superuser: whether user admin or not
        :return email_user.models.EmailUser user: user
        :raise ValueError: email is not set

        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        user = self.model(email=email, is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """ Create and save an EmailUser with the given email and password.

        :param str email: user email
        :param str password: user password
        :return email_user.models.EmailUser user: regular user

        """
        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(email, password, is_staff, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """ Create and save an EmailUser with the given email and password.

        :param str email: user email
        :param str password: user password
        :return email_user.models.EmailUser user: admin user

        """
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class EmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=255,
                              unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = EmailUserManager()


    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """ Return the email."""
        return self.email

    def get_short_name(self):
        """ Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])


#http://stackoverflow.com/questions/21508485/django-authentication-user-returns-none