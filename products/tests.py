from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product

class ProductAPITest(TestCase):
    def setUp(self):
        Product.objects.create(name="Laptop A", category="Electronics", price=1000, description="desc")
        Product.objects.create(name="Mouse", category="Accessories", price=20, description="desc")
        self.client = APIClient()

    def test_search(self):
        resp = self.client.get('/api/products/', {'search': 'laptop'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 1)
