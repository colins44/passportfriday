from .models import EmailUser
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.utils.module_loading import import_by_path
from django.middleware.csrf import rotate_token
from django.contrib.auth.backends import ModelBackend
from django.db.models import get_model



def load_backend(path):
    return import_by_path(path)()

def get_backends():
    backends = []
    for backend_path in settings.AUTHENTICATION_BACKENDS:
        backends.append(load_backend(backend_path))
    if not backends:
        raise ImproperlyConfigured('No authentication backends have been defined. Does AUTHENTICATION_BACKENDS contain anything?')
    return backends

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

# import sys
# import hashlib
# import base64
#
# from django.contrib.auth.backends import ModelBackend
# # from email_user.models import EmailUser
# from django.utils.encoding import force_bytes
#
class EmailUserAuth(ModelBackend):
    def authenticate(self, username=None, password=None):
        print 'thiasjoidjasdljsaldkjj'
        try:
            user = self.user_class.objects.get(email=username)
            print '$$$$$$$$'
            print user
            if user.check_password(password):
                return user
        except self.user_class.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExist:
            return None

    @property
    def user_class(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model(*settings.AUTH_USER_MODEL.split('.', 2))
            if not self._user_class:
                raise ImproperlyConfigured('Could not get custom user model')
        return self._user_class
#
#     def hash_password(self, password, salt):
#         h = hashlib.sha512()
#         salted = '%s{%s}' % (password, salt,)
#         h.update(force_bytes(salted))
#         digest = h.digest()
#
#         for i in range(0, 4999):
#             h = hashlib.sha512()
#             h.update(force_bytes(digest) + force_bytes(salted))
#             digest = h.digest()
#
#         return base64.b64encode(force_bytes(digest))
#
#
#     def authenticate(self, email=None, password=None, **kwargs):
#         try:
#             user = EmailUser.objects.get(email=email)
#         except EmailUser.DoesNotExist:
#             return None
#         salt = user.bfi_salt
#         if user.password == self.hash_password(password, salt):
#             user.set_password(password)
#             user.save()
#             return user
#         return None
#
#     def authenticate(**credentials):
#         """
#         If the given credentials are valid, return a User object.
#         """
#         for backend in get_backends():
#             try:
#                 user = backend.authenticate(**credentials)
#             except TypeError:
#                 print 'typererror'
#                 # This backend doesn't accept these credentials as arguments. Try the next one.
#                 continue
#             except PermissionDenied:
#                 print 'pemission denied'
#                 # This backend says to stop in our tracks - this user should not be allowed in at all.
#                 return None
#             if user is None:
#                 print 'is user none'
#                 continue
#             # Annotate the user object with the path of the backend.
#             user.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
#             return user

        # The credentials supplied are invalid to all backends, fire signal
        # user_login_failed.send(sender=__name__,
        #         credentials=_clean_credentials(credentials))