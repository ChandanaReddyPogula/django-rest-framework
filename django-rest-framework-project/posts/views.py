from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [JSONRenderer]

"""
class PostViewSet(viewsets.ViewSet):

    def list(self, request: Request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        response = {
            'message': 'All posts',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request: Request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request: Request, pk: int):
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post)
        response = {
            'message': 'Post detail',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def update(self, request: Request, pk: int):
        data = request.data
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post updated',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk: int):
        post = get_object_or_404(Post, id=pk)
        post.delete()
        response = {
            'message': 'Post deleted'
        }
        return Response(response, status=status.HTTP_200_OK)


class PostList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)
    
class PostDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request: Request, post_id: int):
        return self.retrieve(request, post_id)

    def put(self, request: Request, post_id: int):
        return self.update(request, post_id)

    def delete(self, request: Request, post_id: int):
        return self.destroy(request, post_id)


class PostList(APIView):
    def get(self, request: Request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        response = {
            'message': 'All posts',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request: Request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get(self, request: Request, post_id: int):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        response = {
            'message': 'Post detail',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request: Request, post_id: int):
        data = request.data
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post updated',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, post_id: int):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        response = {
            'message': 'Post deleted'
        }
        return Response(response, status=status.HTTP_200_OK)

        
@api_view(['GET'])
def all_posts(request: Request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    response = {
        'message': 'All posts',
        'data': serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_post(request: Request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        response = {
            'message': 'Post created',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_post(request: Request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(post)
    response = {
        'message': 'Post detail',
        'data': serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_post(request: Request, post_id: int):
    data = request.data
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
        response = {
            'message': 'Post updated',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request: Request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    response = {
        'message': 'Post deleted'
    }
    return Response(response, status=status.HTTP_200_OK)
"""