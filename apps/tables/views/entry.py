from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from apps.tables.models import Entry
from apps.tables.serializers import EntrySerializer


class EntryViewSet(RetrieveModelMixin,
                   ListModelMixin,
                   CreateModelMixin,
                   DestroyModelMixin,
                   GenericViewSet):
    """
    """
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.all()
