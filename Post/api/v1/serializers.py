from rest_framework import serializers
from Post.models import Post
from django.contrib.auth.models import User

class PostsSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'status', 'author', 'created_at', 'updated_at')