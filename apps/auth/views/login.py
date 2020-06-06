from datetime import datetime

from django.conf import settings

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings as jwt_settings

from apps.auth.serializers import JWTSerializer, LoginSerializer
from apps.auth.utils import jwt_encode


class LoginView(GenericAPIView):
    """
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token = jwt_encode(self.user)

    def get_response(self):
        data = {'user': self.user, 'token': self.token}
        serializer = JWTSerializer(
            instance=data, context={'request': self.request}
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)

        if jwt_settings.JWT_AUTH_COOKIE:
            expiration = (
                datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA
            )
            response.set_cookie(
                jwt_settings.JWT_AUTH_COOKIE,
                self.token,
                expires=expiration,
                httponly=True,
                secure=settings.SECURE_COOKIE
            )

        return response

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=self.request.data, context={'request': request}
        )
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()
