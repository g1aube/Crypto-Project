from rest_framework import generics
from .models import CustomUser, Post
from .serializers import CustomUserSerializer, PostSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# Пользователь публикует новости
class PostModel(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Получение конкретного поста
    def get(self, request, id, format=None):
        post = get_object_or_404(Post,
                                 id=id,
                                 owner=request.user
                                 )
        serializer = PostSerializer(post)
        return Response(serializer.data)

class GetPostsModel(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Получение всех статей пользователя

    def get_object(self):
        post = get_object_or_404(Post, id=self.kwargs['id'], owner=self.request.user)
        return post