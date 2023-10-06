from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post , Category
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.

class PostTests(APITestCase):
    
    def test_view_posts(self):
        
        # Warning : Use .get for check the display of data
        url = reverse('blog_api:listcreate')
        response = self.client.get(url , format='json')
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        
    def create_post(self):
        # category
        self.test_cat = Category.objects.create(name="django")
        # create a new post
        self.test_post = Post.objects.create(category_id = 1,title="Post title",excerpt="Post excerpt" , content="Post content", slug="post-title" , author_id=1 , status="published")
        # data 
        data = {"title":"new" , "author":1, "excerpt":"new" , "content":"new"}
        # url
        # Warning : Use .post for check the save of data
        url = reverse('blog_api:listcreate')
        response = self.client.post(url , data , format='json')
        
        # test
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
        
