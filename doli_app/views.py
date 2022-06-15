from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import authentication, permissions
from .permissions import *
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import AdminUserSerializer, UserSerializer
from rest_framework import authentication, permissions

class AdminUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # http_method_names = ['get', 'put', 'delete',]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]




class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminAuthenticated,]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

