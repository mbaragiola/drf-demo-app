from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from apps.tables.models import Table
from apps.tables.serializers import TableSerializer
from apps.tables.views.filters import TableFilter


class TableViewSet(RetrieveModelMixin,
                   ListModelMixin,
                   CreateModelMixin,
                   DestroyModelMixin,
                   GenericViewSet):
    """
    """
    serializer_class = TableSerializer
    filterset_class = TableFilter
    search_fields = ['table_name_search', ]
    lookup_field = 'table_name'

    def get_queryset(self):
        return Table.objects.all()
