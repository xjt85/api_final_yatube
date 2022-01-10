from django.contrib.auth import get_user_model
from posts.models import Comment, Follow, Group, Post
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #     queryset=User.objects.all(), slug_field='username'
    # )
    # following = serializers.SlugRelatedField(
    #     queryset=User.objects.all(), slug_field='username'
    # )
    user = serializers.StringRelatedField()
    following = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = Follow
