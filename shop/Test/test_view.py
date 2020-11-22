from unittest import TestCase

from shop.models import MyUser
from django.test import Client


class MainViewTestCase(TestCase):

    def setUp(self):
        MyUser.objects.create_user('vas', 1111, )
        self.c = Client()

    def test_login_correct(self):
        response = self.c.post('/login/', {'username': 'vas', 'password': 1111})
        self.assertEqual(response.status_code, 302)

    def test_login_incorrect(self):
        response = self.c.post('/login/', {'username': 'vas', 'password': 11})
        errors = response.context.get('form').errors
        self.assertIsNotNone(errors)


