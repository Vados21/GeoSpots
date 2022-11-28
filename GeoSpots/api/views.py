from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from .serializers import PostSerializer
from rest_framework import status

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

#@api_view(['POST'])
#def create_post(request):
#    data = request.data
#   post = Post.objects.create(
#        title=data['title'],
#        text=data['text'],
#        lat=data['lat'],
 #       lon=data['lon']
#    )
#    serializer = PostSerializer(post, many=False)
#    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_post(request, pk):

    data = request.data

    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


