from django.test import TestCase
from django.contrib.auth.models import User
from ecommerce.models import Category , Product , Order

# Create your tests here.


class ProductTest(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        
        test_user = User.objects.create_user(username="test_user" , password="pwduser")
        test_cat = Category.objects.create(name = "django")
        test_prod = Product.objects.create(title="product1" , description="product1" , price=199, qte = 2 , category_id = 1)
        # return super().setUpTestData()
        
        test_order = Order.objects.create(user = test_user , product = test_prod , quantity = 1)
    
    def test_products(self):
        
        prod = Product.objects.get(id = 1)
        cat = Category.objects.get(id = 1)
        
        # 
        cat_name = f'{cat.name}'
        # 
        title_prod = f'{prod.title}'
        desc_prod = f'{prod.description}'
        price_prod = prod.price
        qte_prod = prod.qte
        
        # 
        self.assertEqual(cat.name , cat_name)
        # 
        self.assertEqual(prod.title , title_prod)
        self.assertEqual(prod.description , desc_prod)
        self.assertEqual(prod.price , price_prod)
        self.assertEqual(prod.qte , qte_prod)
        pass
    
    def test_orders(self):
        
        # prod = Product.objects.get(id = 1)
        # cat = Category.objects.get(id = 1)
        order = Order.objects.get(id = 1)
        # user = User.objects.get(id = 1)
        
        user_order = f'{order.user}'
        prod_order = f'{order.product}'
        qte_order = order.quantity
        
        self.assertEqual(str(order.product) , prod_order)
        self.assertEqual(order.quantity , qte_order)
        self.assertEqual(str(order.user) , user_order)
        
        
        pass