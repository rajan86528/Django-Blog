from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.forms import UserRegistrationForm

# Create your tests here.


class AccountsCreationTest(TestCase):

    def setUp(self):
        self.form_class = UserRegistrationForm

    def test_singup_page_exist(self):
        response  = self.client.get(reverse('signup_page'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response, 'Create your account')

    def test_signup_form_works_correctly(self):

        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        sample_data =  {
            'email': 'test01@gmail.com',
            'username': 'test01',
            'password1': 'pass@123',
            'password2': 'pass@123', 
        } 

        form = self.form_class(sample_data)

        self.assertTrue(form.is_valid())



    def test_signup_form_create_userin_db(self):
        user =  {
            'email': 'test02@gmail.com',
            'username': 'test02',
            'password1': 'pass@123',
            'password2': 'pass@123', 
        }

        form = self.form_class(user)
        User = get_user_model()
        if form.is_valid:
            form.save()
        
        self.assertEqual(User.objects.count(), 1)