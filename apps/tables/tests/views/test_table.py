from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.tables.models import Table
from apps.users.tests.factories import UserFactory


class TableTestCase(APITestCase):
    """
    Test basic API endpoint functionalities for Table.
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()

        # This should have its own factory, but this will do.
        cls.table = Table.objects.create(
            table_name='movies',
            fields={
                'title': {
                    'field_type': 'str',
                    'is_unique': True
                },
                'release_date': 'datetime',
                'imdb_ranking': 'float',
                'director': {
                    'field_type': 'int',
                    'foreign_key': 'directors.id'
                }
            }
        )

        cls.valid_data = {
            'table_name': 'another_table',
            'fields': {
                'field_one': {'field_type': 'str', 'primary_key': True},
                'field_two': 'int'
            }
        }

        cls.table_url = reverse('api:tables:table-detail', args=[cls.table.table_name])
        cls.table_list_url = reverse('api:tables:table-list')

    def test_read_detail_anon(self):
        self.client.logout()

        response = self.client.get(self.table_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_read_list_anon(self):
        self.client.logout()

        response = self.client.get(self.table_list_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_read_detail_user(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.table_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['table_name'] == self.table.table_name
        assert response.data['fields'] == self.table.fields

    def test_read_list_user(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.table_url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_anon(self):
        self.client.logout()

        response = self.client.post(self.table_list_url, self.valid_data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_user_successful(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.table_list_url, self.valid_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['table_name'] == self.valid_data['table_name']
        assert response.data['fields'] == self.valid_data['fields']

    def test_create_user_table_name_already_taken(self):
        self.client.force_authenticate(user=self.user)
        data = {'table_name': self.table.table_name, 'fields': self.table.fields}

        response = self.client.post(self.table_list_url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_update_anon(self):
        self.client.logout()

        response = self.client.put(self.table_url, self.valid_data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        response = self.client.patch(self.table_url, self.valid_data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_user(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.put(self.table_url, self.valid_data, format='json')
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

        response = self.client.patch(self.table_url, self.valid_data, format='json')
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_delete_anon(self):
        self.client.logout()

        response = self.client.delete(self.table_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_user(self):
        self.client.force_authenticate(user=self.user)
        table = Table.objects.create(table_name='t', fields={'min': 'str'})
        table_url = reverse('api:tables:table-detail', args=[table.table_name])

        response = self.client.delete(table_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Table.objects.filter(table_name='t').exists() is False
