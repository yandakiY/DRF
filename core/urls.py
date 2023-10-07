
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/' , include('blog.urls' , namespace="blog")),
    path('api/' , include('blog_api.urls', namespace="blog_api")),
    path('ecom/' , include('ecommerce.urls' , namespace="ecom")),
    path('api_ecom/' , include('ecommerce_api.urls' , namespace='ecom_api'))
]
