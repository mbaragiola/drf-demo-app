from rest_framework.serializers import ModelSerializer

from apps.tables.models import Table


class TableSerializer(ModelSerializer):

    class Meta:
        model = Table
        fields = ['table_name', 'fields', ]
