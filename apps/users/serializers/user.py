from rest_framework.serializers import ModelSerializer
from apps.users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', ]
        extra_kwargs = {
            'username': {'read_only': True},
            'email': {'read_only': True},
        }
