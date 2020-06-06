from datetime import datetime

from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer,
    RefreshJSONWebTokenSerializer,
    VerifyJSONWebTokenSerializer,
)
from rest_framework_jwt.views import (
    JSONWebTokenAPIView,
    jwt_response_payload_handler,
)

__all__ = [
    'ObtainJSONWebToken',
    'VerifyJSONWebToken',
    'RefreshJSONWebToken',
]


class CustomJSONWebTokenAPIView(JSONWebTokenAPIView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if settings.JWT_AUTH['JWT_AUTH_COOKIE']:
                expiration = (datetime.utcnow() +
                              settings.JWT_AUTH['JWT_EXPIRATION_DELTA'])
                response.set_cookie(
                    settings.JWT_AUTH['JWT_AUTH_COOKIE'],
                    token,
                    expires=expiration,
                    httponly=True,
                    secure=settings.SECURE_COOKIE,
                )
                response.cookies[
                    settings.JWT_AUTH['JWT_AUTH_COOKIE']
                ]['samesite'] = settings.JWT_AUTH['JWT_COOKIE_SAMESITE']
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainJSONWebToken(CustomJSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer


class VerifyJSONWebToken(CustomJSONWebTokenAPIView):
    """
    API View that checks the veracity of a token, returning the token if it
    is valid.
    """
    serializer_class = VerifyJSONWebTokenSerializer


class RefreshJSONWebToken(CustomJSONWebTokenAPIView):
    """
    API View that returns a refreshed token (with new expiration) based on
    existing token

    If 'orig_iat' field (original issued-at-time) is found, will first check
    if it's within expiration window, then copy it to the new token
    """
    serializer_class = RefreshJSONWebTokenSerializer
