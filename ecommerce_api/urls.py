
from django.contrib import admin
from django.urls import path , include
from .views import ProductView , ProductCreate , ProductDetail , OrderView ,OrderCreate , OrderDetails


app_name = "ecom_api"

urlpatterns = [
    path('' , ProductView.as_view() , name="listcreate"),
    path('create/' , ProductCreate.as_view() , name="create"),
    path('<int:pk>/' , ProductDetail.as_view() , name="detailproduct"),
    path('orders/' , OrderView.as_view() , name="listcreateorders"),
    path('orders/create' , OrderCreate.as_view() , name="createorders"),
    path('orders/<int:pk>' , OrderDetails.as_view() , name="detailorder"),

]
