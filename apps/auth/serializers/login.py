from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            raise ValidationError(
                {'non_field_errors': ['You must include useername and password.']}
            )

        if not user:
            raise ValidationError({'non_field_errors': ['Wrong credentials.']})
        elif not user.is_active:
            raise ValidationError({'non_field_errors': ['Disabled account.']})

        attrs['user'] = user
        return attrs
