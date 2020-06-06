from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.tables.models import Table
from apps.users.tests.factories import UserFactory


class EntryTestCase(APITestCase):
    """
    Test basic API endpoint functionalities for Entry.
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
            'title': 'The Title',
            'director': 1,
            'imdb_ranking': 7.3,
            'release_date': '1990-08-27',
        }

        cls.entry_list_url = reverse('api:tables:entry-list', args=[cls.table.table_name])

    def test_read_list_anon(self):
        self.client.logout()

        response = self.client.get(self.entry_list_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_read_list_user(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.entry_list_url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_anon(self):
        self.client.logout()

        response = self.client.post(self.entry_list_url, self.valid_data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_user_successful(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.entry_list_url, self.valid_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['table'] == self.table.pk
