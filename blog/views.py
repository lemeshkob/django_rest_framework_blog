from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer


@permission_classes((permissions.AllowAny,))
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@permission_classes((permissions.AllowAny,))
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
