from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """
    BlogPost serializer
    Serializes/Deserializes model fields to JSON or vice versa
    owner - ReadOnlyField of the userObject
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'content', 'created', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User serializer
    Serializes/Deserializes model fields to JSON or vice versa
    BlogPosts - All users' BlogPosts
    """

    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts')
