from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginTest(TestCase):

    def setUp(self):
        self.username = 'test03'
        self.email = 'test03@gmail.com'
        self.password = 'pass@123'

        User.objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password,
        )



    def test_login_page_exist(self):
        response = self.client.get(reverse('login_page'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_page_has_login_from(self):
        response = self.client.get(reverse('login_page'))

        form = response.context.get('form')
        self.assertIsInstance(form, AuthenticationForm)

    def test_login_page_logs_in_user(self):
        user_data = {
            'username': self.username,
            'password': self.password
        }

        response = self.client.post(reverse('login_page'), user_data)
        self.assertRedirects(response, reverse('homepage'))
        