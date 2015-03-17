# from django.contrib.auth import authenticate, login
# import jwt
#
# class TokenMiddleware( object ):
#     """
#     Authentication Middleware for JWT Tokens
#     """
#     def process_request(self, request):
#         if 'HTTP_AUTHORIZATION' in request.META:
#             auth = request.META.get('HTTP_AUTHORIZATION')
#             parts = auth.split()
#             if parts[0] == 'JWT':
#                 user = authenticate(token=parts[1])
#                 if user:
#                     request.user = user
