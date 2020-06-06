from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tables.models import Entry
from apps.tables.serializers import EntrySerializer


class EntriesByTableList(ListCreateAPIView):
    serializer_class = EntrySerializer
    lookup_field = 'table_name'

    def create(self, request, *args, **kwargs):
        data = {'data': request.data}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        table_name = self.kwargs.get('table_name')
        return Entry.objects.filter(table__table_name=table_name).all()

    def get_serializer_context(self):
        context = super(EntriesByTableList, self).get_serializer_context()
        context['table_name'] = self.kwargs.get('table_name')
        return context


class QueryTableView(APIView):

    def post(self, request, table_name=None):
        queryset = Entry.objects.filter(
            table__table_name=table_name,
            data__contains=request.data
        )
        serializer = EntrySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
