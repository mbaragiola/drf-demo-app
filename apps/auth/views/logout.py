from django.contrib.auth import logout as django_logout
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.settings import api_settings as jwt_settings

__all__ = ['LogoutViewSet']


class LogoutViewSet(GenericViewSet):
    """
    Calls Django logout method and deletes the token
    assigned to the current User object.
    Accepts/Returns nothing.
    """
    permission_classes = (AllowAny,)
    serializer_class = None

    @action(detail=False, methods=['post'])
    def alldevices(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        django_logout(request)
        response = Response(
            {"detail": "You've been logged out from all devices."},
            status=status.HTTP_200_OK
        )
        response.delete_cookie(jwt_settings.JWT_AUTH_COOKIE)

        return response

    @action(detail=False, methods=['post'])
    def cookie(self, request):
        response = Response(
            {"detail": "You've been logged out from this device."},
            status=status.HTTP_200_OK
        )
        response.delete_cookie(jwt_settings.JWT_AUTH_COOKIE)
        return response

    @action(detail=False, methods=['post'])
    def token(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        return Response(
            {"detail": "You've been logged out from this device."},
            status=status.HTTP_200_OK
        )
