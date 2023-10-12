from django.db import models
from rest_framework.generics import ListAPIView , CreateAPIView , ListCreateAPIView , RetrieveAPIView
from ecommerce.models import Product , Order
from .serializers import ProductSerializer , ProductCreateSerialize , OrderSerializer , OrderCreateSerializer
# Create your models here.

class ProductView(ListAPIView):
    queryset = Product.postobjects.all()
    serializer_class = ProductSerializer
    
    pass

class ProductCreate(CreateAPIView):
    queryset = Product.postobjects.all()
    serializer_class = ProductCreateSerialize
    

class ProductDetail(RetrieveAPIView):
    queryset = Product.postobjects.all()
    serializer_class = ProductSerializer
    
    pass

class OrderView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    pass

class OrderDetails(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer