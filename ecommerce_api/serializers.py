from rest_framework import serializers
from ecommerce.models import Product
from rest_framework.fields import CharField , IntegerField


class ProductSerializer(serializers.ModelSerializer):
    
    name = CharField(source="title" , required="True")
    quantity = IntegerField(source="qte", required="True")
    
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'quantity',
            'category',
            'description',
            'status'
        )