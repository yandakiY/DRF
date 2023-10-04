from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pass



"""
Concrete View Classes
The following classes are the concrete generic views. If you're using generic views this is normally the level you'll be working at unless you need heavily customized behavior.

The view classes can be imported from rest_framework.generics.

CreateAPIView
Used for create-only endpoints.

Provides a post method handler.

Extends: GenericAPIView, CreateModelMixin

ListAPIView
Used for read-only endpoints to represent a collection of model instances.

Provides a get method handler.

Extends: GenericAPIView, ListModelMixin

RetrieveAPIView
Used for read-only endpoints to represent a single model instance.

Provides a get method handler.

Extends: GenericAPIView, RetrieveModelMixin

DestroyAPIView
Used for delete-only endpoints for a single model instance.

Provides a delete method handler.

Extends: GenericAPIView, DestroyModelMixin

UpdateAPIView
Used for update-only endpoints for a single model instance.

Provides put and patch method handlers.

Extends: GenericAPIView, UpdateModelMixin

ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.

Provides get and post method handlers.

Extends: GenericAPIView, ListModelMixin, CreateModelMixin

RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.

Provides get, put and patch method handlers.

Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin

RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.

Provides get and delete method handlers.

Extends: GenericAPIView, RetrieveModelMixin, DestroyModelMixin

RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.

Provides get, put, patch and delete method handlers.

Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
"""