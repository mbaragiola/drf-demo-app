from rest_framework.mixins import (
    CreateModelMixin,
    DeleteModelMixin,
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
                   DeleteModelMixin,
                   GenericViewSet):
    """
    """
    serializer_class = TableSerializer
    filterset_class = TableFilter
    search_fields = ['table_name_search', ]

    def get_queryset(self):
        return Table.objects.all()
