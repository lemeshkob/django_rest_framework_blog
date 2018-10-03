from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """
    BlogPost serializer
    Serializes/Deserializes model fields to JSON or vice versa
    owner - ReadOnlyField of the userObject
    """

    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'content', 'created', 'owner', 'comments')


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


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ('url', 'author', 'content', 'created', 'post')
