from rest_framework.serializers import ModelSerializer

from apps.tables.models import Entry, Table


class EntrySerializer(ModelSerializer):

    class Meta:
        model = Entry
        fields = ['table', 'data', ]
        extra_kwargs = {
            'table': {'read_only': True},
        }

    # TODO: Validation could be added here.

    def create(self, validated_data):
        validated_data['table'] = Table.objects.get(
            table_name=self.context.get('table_name')
        )
        return Entry.objects.create(**validated_data)
