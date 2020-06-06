from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.users.tests.factories import UserFactory


class LogoutTestCase(APITestCase):
    """
    Test JWT logout.
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.logout_url = reverse('api:auth:logout-alldevices')
        cls.logout_cookie_url = reverse('api:auth:logout-cookie')
        cls.logout_token_url = reverse('api:auth:logout-token')

    def test_successful(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.logout_url)
        assert response.status_code == status.HTTP_200_OK

    def test_cookie_successful(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.logout_cookie_url)
        assert response.status_code == status.HTTP_200_OK

    def test_token_successful(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.logout_token_url)
        assert response.status_code == status.HTTP_200_OK

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.logout_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_cookie_wrong_method(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.logout_cookie_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_token_wrong_method(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.logout_token_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
