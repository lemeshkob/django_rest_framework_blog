from rest_framework import permissions, generics
from .models import Post, Comment
from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })


class PostList(generics.ListCreateAPIView):
    """
    BlogPost list display class
    Allows to retrieve all BlogPost objects and crete one
    permissions_classes - classes which are operating the permissions of BlogPost object (owner or not)
    queryset - queryset to all user objects
    serializer_class - serializer class that class uses for view
    """
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    BlogPostDetail class allows ro Retrieve Update Destroy single BlogPost object\n
    permissions_classes - classes which are operating the permissions of BlogPost object (owner or not)\n
    queryset - queryset to all BlogPost objects\n
    serializer_class - serializer class that class uses for view
    """
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListAPIView):
    """
    User list display
    queryset - queryset to all user objects
    serializer_class - serializer class that class uses for view
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    UserDetail class allows ro Retrieve single User object
    queryset - queryset to all user objects
    serializer_class - serializer class that class uses for view
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentList(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )


def posts_view(request):
    return render(request, 'posts/posts.html')