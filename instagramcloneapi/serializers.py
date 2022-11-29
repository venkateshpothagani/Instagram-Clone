# from django.contrib.auth.models import User, Group
from instagramcloneapi.models import User, Post, Profile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     class Meta:
#         model = User
#         fields = ['id', 'url', 'username', 'email', 'groups', 'posts']


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

# class PostSerializer(serializers.ModelSerializer):
#     # user = serializers.ReadOnlyField(source='user.username')
#     image_url = serializers.ImageField(required=False)

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'body', 'image_url']

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image')

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('id', 'username', 'name', 'image')

class UserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
