from rest_framework.test import APITestCase
from rest_framework import status
from ecommerce.models import Product, Category, Order
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class ApiProductTest(APITestCase):
    
    def setUp(self) -> None:
        
        test_user = User.objects.create_user(username="test_user" , password="pwd_user")
        test_cat = Category.objects.create(name="django")
        # return super().setUp()
    
    def test_views_products(self):
        
        url = reverse('ecom_api:list')
        response = self.client.get(url)

        # print(response.content)
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        # pass
    
    def test_create_product(self):
        
        
        data = {"name":"product1","description":"product1","price":100,"quantity":2}
        url = reverse("ecom_api:create")
        
        response = self.client.post(url , data)
        # print(response.content)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
        # pass