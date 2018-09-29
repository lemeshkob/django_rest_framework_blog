from rest_framework import generics
from rest_framework import permissions
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


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
    BlogPostDetail class allows ro Retrieve Update Destroy single BlogPost object
    permissions_classes - classes which are operating the permissions of BlogPost object (owner or not)
    queryset - queryset to all BlogPost objects
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
