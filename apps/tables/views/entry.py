from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView

from apps.tables.models import Entry
from apps.tables.serializers import EntrySerializer


class EntryViewSet(RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    """
    """
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.all()


class EntriesByTableList(ListCreateAPIView):
    serializer_class = EntrySerializer
    lookup_field = 'table_name'

    def get_queryset(self):
        table_name = self.kwargs.get('table_name')
        return Entry.objects.filter(table__table_name=table_name).all()

    def get_serializer_context(self):
        context = super(EntriesByTableList, self).get_serializer_context()
        context['table_name'] = self.kwargs.get('table_name')
        return context
