from django.test import TestCase

from .models import Customer, Teller


class CustomerTestCase(TestCase):
    def setUp(self):
        teller = Teller.objects.create(name="Fabrice", wait_time=10)
        customer = Customer()
        customer.name = "delyce"
        customer.teller = teller
        customer.save()

    def test_customer_get_delete_url(self):
        customer = Customer.objects.get(name="delyce")
        self.assertEqual(customer.get_delete_url(), "/delete/%s" % customer.id)
