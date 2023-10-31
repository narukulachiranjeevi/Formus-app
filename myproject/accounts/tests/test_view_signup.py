from django.contrib.auth.models import User
from django.urls import resolve
from django.test import TestCase

from ..views import signup
from ..forms import SignUpForm
from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve
from django.test import TestCase

class SignUp(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_signup_url_resolves_signup_view(self):
        view = resolve(reverse('signup'))
        self.assertEqual(view.func,signup)

    def test_csrf(self):
        self.assertEqual(self.response,'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm) 



class SignUpTests(TestCase):
    # code suppressed...
    pass


class SuccessfulSignUpTests(TestCase):
   def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  # submit an empty dictionary

    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())










