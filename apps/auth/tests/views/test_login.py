from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.users.tests.factories import UserFactory


class LoginTestCase(APITestCase):
    """
    Test JWT login.
    """
    @classmethod
    def setUpTestData(cls):
        cls.login_url = reverse('api-v1:auth:login')
        cls.user = UserFactory()
        cls.user_password = 'Hola.Chau'
        cls.user.set_password(cls.user_password)
        cls.user.save(update_fields=['password'])

    def test_successful(self):
        self.client.logout()

        data = {
            'username': self.user.username,
            'password': self.user_password
        }
        response = self.client.post(self.login_url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['user']['id'] == self.user.id
        assert response.data['token'] is not None
        assert response.data['token'] != ''

    def test_wrong_credentials(self):
        self.client.logout()

        data = {'username': self.user.username, 'password': 'asd'}
        response = self.client.post(self.login_url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_disabled(self):
        self.client.logout()
        self.user.is_active = False
        self.user.save(update_fields=['is_active'])

        data = {
            'username': self.user.username,
            'password': self.user_password
        }
        response = self.client.post(self.login_url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        self.user.is_active = True
        self.user.save(update_fields=['is_active'])
