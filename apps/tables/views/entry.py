from rest_framework.mixins import (
    CreateModelMixin,
    DeleteModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from apps.tables.models import Entry
from apps.tables.serializers import EntrySerializer


class EntryViewSet(RetrieveModelMixin,
                   ListModelMixin,
                   CreateModelMixin,
                   DeleteModelMixin,
                   GenericViewSet):
    """
    """
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.all()
