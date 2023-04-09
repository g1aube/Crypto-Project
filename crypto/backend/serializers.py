from rest_framework import serializers
from .models import CustomUser, Post

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'phone_number',
            'address'
        ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'owner',
            'public',
            'category',
            'date'
        ]
        read_only_fields = ['owner']