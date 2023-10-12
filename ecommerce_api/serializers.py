from rest_framework import serializers
from ecommerce.models import Product , Order
from rest_framework.fields import DateTimeField , CharField , IntegerField


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


# serializer for create product 
class ProductCreateSerialize(serializers.ModelSerializer):
    
    name = CharField(source = "title")
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'category',
            'status',
        ]


class OrderCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Order
        fields = ['product' , 'quantity' , 'user']     
        

class OrderSerializer(serializers.ModelSerializer):
    
    # date_activate = DateTimeField(source="activate_date")
    # user = CharField(source="user.username")
    name_user = serializers.CharField(source="user.username")
    mail_user = serializers.CharField(source="user.email")
    product = CharField(source = "product.title")
    
    class Meta:
        model = Order
        fields = [
            'id',
            'product',
            'quantity',
            'user',
            'name_user',
            'mail_user'
        ]