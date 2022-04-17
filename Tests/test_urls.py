from urllib import response
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY


class TestUrls(TestCase):
    def testHomePage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testAdmin(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 301)

    def setUp(self):
        self.credentials = {
            'username': 'delyce',
            'password': '1234'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post(
            '/admin/register/', self.credentials, follow=True)
        # should be logged in now
        self.assertEqual(response.status_code, 200)
