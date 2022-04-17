from django.test import Client, TestCase
from .models import Teller


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Teller.objects.create(name="Delyce", wait_time=10)
        Teller.objects.create(name="Fabrice", wait_time=20)
        self.teller = Teller.objects.create(name="Muhire", wait_time=1)

    def testHomepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tellers"]), 3)

    def test_teller_view(self):
        response = self.client.get(self.teller.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["customers"]), 0)

    def test_teller_view_error(self):
        response = self.client.get("/queue/123")
        res1 = self.client.get("/queue/12f")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res1.status_code, 404)

    def test_registering(self):
        response = self.client.get("%s?name=Fabrice" %
                                   self.teller.get_register_url())
        # You will be redirected on success
        self.assertEqual(response.status_code, 302)
