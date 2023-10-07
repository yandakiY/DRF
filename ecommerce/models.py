from django.db import models
from django_extensions.db.models import (
    TitleSlugDescriptionModel , ActivatorModel , TimeStampedModel
)


# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'{self.name}'
    

class Product(TitleSlugDescriptionModel , ActivatorModel , TimeStampedModel):
    
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="Price product", decimal_places=3 , max_digits=16)
    qte = models.IntegerField(verbose_name="Quantity product")
    
    
    def __str__(self) -> str:
        return f'{self.title}'
    