from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('c3po', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um usuário com as credenciais corretas"""
        user = authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)
