from rest_framework.test import APITestCase
from rest_framework import status
from ecommerce.models import Product, Category, Order
from django.urls import reverse
from django.contrib.auth.models import User
import json
# Create your tests here.

class ApiProductTest(APITestCase):
    
    def setUp(self) -> None:
        
        test_prod = Product.objects.create(title = "product" , description = "product" , price = "100.000" , qte = 2)
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
    
    def test_one_product(self):
        
        url = reverse('ecom_api:detailproduct' , args=(1,))
        response = self.client.get(url , format="json")
        
        # get value name and price
        data = json.loads(response.content.decode("utf-8"))
        
        # print(response.content)
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertEqual(data['name'] , "product")
        self.assertEqual(data['description'] , "product")
        self.assertEqual(data['price'] , "100.000")
        
    
    def test_no_this_product(self):
        
        url = reverse('ecom_api:detailproduct' , args=(2,))
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)
        
        
class ApiOrderTest(APITestCase):
    
    
    def setUp(self) -> None:
        
        test_user = User.objects.create_user(username="test_user" , password="pwd_user")
        test_cat = Category.objects.create(name="django")
        test_prod = Product.objects.create(title="product" , description="product description" ,price = "100.000" , qte = 2)
        test_prod1 = Product.objects.create(title="product1" , description="product1 description" ,price = "100.000" , qte = 1)
        test_order = test_prod.place_order(test_user , 1)
        # test_order1 = test_prod1.place_order(test_user , 1)
        
        # return super().setUp()
        
    
    def test_views_orders(self):
        
        url = reverse("ecom_api:listcreateorders")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code , status.HTTP_200_OK)
    
    def test_one_order(self):
        
        url = reverse("ecom_api:detailorder" , args=(1,))
        prod = Product.objects.get(id = 1)
        order = Order.objects.get(id = 1)
        response = self.client.get(url)
        
        # get data
        data = json.loads(response.content.decode("utf-8"))
        
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertEqual(data["product"] , prod.title)
        self.assertEqual(data['quantity'] , order.quantity)
    
    def test_not_this_order(self):
        
        url = reverse("ecom_api:detailorder" , args=(3,))
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)
    
    