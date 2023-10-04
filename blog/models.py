from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Post(models.Model):
    category = models.ForeignKey(Category , on_delete=models.PROTECT , default=1 )
    