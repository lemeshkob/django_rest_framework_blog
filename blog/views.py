from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    Post list display class
    Allows to retrieve all Post objects and crete one
    permissions_classes - classes which are operating the permissions of post object (owner or not)
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
    PostDetail class allows ro Retrieve Update Destroy single Post object
    permissions_classes - classes which are operating the permissions of post object (owner or not)
    queryset - queryset to all post objects
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
