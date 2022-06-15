from asyncore import read
from .models import Post, Comment,User
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user',]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user',]

class UserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = User
        fields = ['username', 'password', ]
        
    def create(self, validated_data):
        admin = User(
            username =validated_data['username']
        )
        admin.set_password(validated_data['password'])
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
        return admin

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        admin = User(
            username =validated_data['username']
        )
        admin.set_password(validated_data['password'])
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
        return admin