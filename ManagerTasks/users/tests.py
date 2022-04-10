# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()     


class UserTestCase(TestCase):
    def setUp(self):
        user = User(
            username='admin'
        )
        user.set_password('admin123')
        user.save()

        """
        Verifia que el usuario pueda iniciar sesión
        """

        client = APIClient()
        response = client.post(
                '/api/token/', {
                'username': 'admin',
                'password': 'admin123',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.access = result['access']
        self.refresh = result['refresh']
    

    def test_token_refresh_user(self):
        """
        Verifia que el usuario pueda iniciar sesión
        """
        client = APIClient()
        response = client.post(
                '/api/token/refresh/', {
                'refresh': self.refresh
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = json.loads(response.content)
        self.access_token = result['access']
