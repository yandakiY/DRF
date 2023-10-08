from django.contrib import admin
from ecommerce.models import Category , Product

# Register your models here.

@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'description' , 'price' , 'status' , 'category') 
    pass


admin.site.register(Category)
