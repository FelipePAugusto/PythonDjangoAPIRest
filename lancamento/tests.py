from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


# Create your tests here.
class TestLancamento(APITestCase):
    def setUp(self):
        self.url = '/lancamentoviewapi/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)   
        self.token.save()
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) 

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )
    
    def test_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)