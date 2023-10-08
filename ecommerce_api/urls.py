
from django.contrib import admin
from django.urls import path , include
from .views import ProductView


app_name = "ecom_api"

urlpatterns = [
    path('' , ProductView.as_view() , name="listcreate"),
    # path('<int:pk>/' , ProductDetail.as_view() , name="detailproduct")
]
