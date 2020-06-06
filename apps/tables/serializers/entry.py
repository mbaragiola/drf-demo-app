from rest_framework.serializers import ModelSerializer

from apps.tables.models import Entry


class EntrySerializer(ModelSerializer):

    class Meta:
        model = Entry
        fields = ['table', 'data', ]
