from django_filters import CharFilter, FilterSet

from apps.tables.models import Table


class TableFilter(FilterSet):
    table_name = CharFilter(
        field_name='table_name',
    )

    class Meta:
        model = Table
        fields = ['table_name']
