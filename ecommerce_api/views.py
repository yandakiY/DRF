from django.db import models
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from ecommerce.models import Product
from .serializers import ProductSerializer
# Create your models here.

class ProductView(ListCreateAPIView):
    queryset = Product.postobjects.all()
    serializer_class = ProductSerializer
    
    pass


class ProductDetail(RetrieveAPIView):
    queryset = Product.postobjects.all()
    serializer_class = ProductSerializer
    
    pass