# from django.test import TestCase
# from django.contrib.auth.models import User
# from blog.models import Category , Post
# # Create your tests here.

# class Test_create_post(TestCase):
    
#     @classmethod
#     def setUpTestData(cls) -> None:
#         cat = Category.objects.create(name="django")
#         user = User.objects.create_user(username="test_user", password="12345")
#         post = Post.objects.create(category_id = 1,title="Post title",excerpt="Post excerpt" , content="Post content", slug="post-title" , author_id = 1 , status="published")

    
#     def test_blog_content(self):
#         post = Post.postobjects.get(id = 1)
#         cat = Category.objects.get(id = 1)
        
#         author = f'{post.author}'
#         title = f'{post.title}'
#         content = f'{post.content}'
#         excerpt = f'{post.excerpt}'
#         status = f'{post.status}'
        
#         # tests
#         self.assertEqual(author , "test_user")
#         self.assertEqual(title , "Post title")
#         self.assertEqual(content , "Post content")
#         self.assertEqual(excerpt , "Post excerpt")
#         self.assertEqual(status , "published")
#         self.assertEqual(str(post) , "Post title")
#         self.assertEqual(str(cat) , "django")
        
        