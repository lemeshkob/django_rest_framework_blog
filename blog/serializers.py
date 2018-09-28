from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    """
    BlogPost serializer
    Serializes/Deserializes model fields to JSON or vice versa
    owner - ReadOnlyField of the userObject
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created', 'owner')


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    Serializes/Deserializes model fields to JSON or vice versa
    BlogPosts - All users' BlogPosts
    """

    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
