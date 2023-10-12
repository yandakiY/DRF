from django.db import models
from django.db.models.query import QuerySet
from django_extensions.db.models import (
    TitleSlugDescriptionModel , ActivatorModel , TimeStampedModel
)

from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'{self.name}'
    

class Product(TitleSlugDescriptionModel , ActivatorModel , TimeStampedModel):
    
    class PostManager(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset() .filter(status = 1)
    
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="Price product", decimal_places=3 , max_digits=16)
    qte = models.IntegerField(verbose_name="Quantity product")
    
    objects = models.Manager()
    postobjects = PostManager()
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    # we need to add new functions: manage_stock, check_stock and place_order
    
    # Substract quantity
    def manage_stock(self , qte):
        my_qte = self.qte
        self.qte = my_qte - qte
        
        self.save()
        
    # check if params qte is great than self.qte
    def check_stock(self , qte):
        if self.qte > int(qte):
            return True
        
        return False
    
    # place order : place our product in a basket with the user and quantity
    def place_order(self , user , qte):
        # test if qte is not great than qte
        if self.check_stock(qte):
            order = Order.objects.create(
                user = user,
                quantity = qte,
                product = self
            )
            
            return order
        return None
    
    
    

class Order(TimeStampedModel , ActivatorModel):
    
    # property
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f'{self.user.username} - {self.product.title}'