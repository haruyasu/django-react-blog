from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'created')
        extra_kwargs = {'author': {'read_only': True}}
