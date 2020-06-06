from rest_framework.serializers import CharField, Serializer

from apps.users.serializers import UserSerializer


class JWTSerializer(Serializer):
    """
    """
    token = CharField()
    user = UserSerializer(read_only=True)
