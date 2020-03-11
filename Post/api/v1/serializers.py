from rest_framework import serializers
from Post.models import Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'status', 'author', 'created_at', 'updated_at')