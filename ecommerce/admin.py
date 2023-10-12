from django.contrib import admin
from ecommerce.models import Category , Order , Product

# Register your models here.

@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'description' , 'price' , 'status' , 'category') 
    pass


admin.site.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id' , 'Product' , 'Quantity')
    
admin.site.register(Category)
