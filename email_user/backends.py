from .models import EmailUser


# class EmailUserAuth(object):
#
#     def authenticate(self, email=None, password=None):
#         try:
#             user = EmailUser.objects.get(email=email)
#             print user.check_password(password)
#             if user.check_password(password):
#                 return user
#         except EmailUser.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         try:
#             user = EmailUser.objects.get(pk=user_id)
#             if user.is_active:
#                 return user
#             return None
#         except EmailUser.DoesNotExist:
#             return None

# class ModelBackend(object):
#     """
#     Authenticates against settings.AUTH_USER_MODEL.
#     """
#
#     def authenticate(self, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)
#         try:
#             user = UserModel._default_manager.get_by_natural_key(username)
#             if user.check_password(password):
#                 return user
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user (#20760).
#             UserModel().set_password(password)

import sys
import hashlib
import base64

from django.contrib.auth.backends import ModelBackend
# from email_user.models import EmailUser
from django.utils.encoding import force_bytes

class EmailUserAuth(ModelBackend):

    def hash_password(self, password, salt):
        h = hashlib.sha512()
        salted = '%s{%s}' % (password, salt,)
        h.update(force_bytes(salted))
        digest = h.digest()

        for i in range(0, 4999):
            h = hashlib.sha512()
            h.update(force_bytes(digest) + force_bytes(salted))
            digest = h.digest()

        return base64.b64encode(force_bytes(digest))


    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = EmailUser.objects.get(email=email)
        except EmailUser.DoesNotExist:
            return None
        salt = user.bfi_salt
        if user.password == self.hash_password(password, salt):
            user.set_password(password)
            user.save()
            return user
        return None