from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Post.models import Post
from django.contrib.auth.models import User
from .serializers import PostsSerializer

class PostList(APIView):
    def get(self, request):
        model = Post.objects.all()
        serializer = PostsSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostsSerializer(data=request.data)
  
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)             
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)        


@api_view(['GET', ])
def api_detail_post_view(request, title):
    try:
        target_post = Post.objects.get(title=title)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)        
    
    if request.method == "GET":
        serializer = PostsSerializer(target_post)
        return Response(serializer.data)

@api_view(['GET', ])
def api_posts_view(request):
    try:
        target_post = Post.objects.all()
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)        
    
    if request.method == "GET":
        serializer = PostsSerializer(target_post)
        return Response(serializer.data)       