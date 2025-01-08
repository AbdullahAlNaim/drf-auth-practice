from rest_framework import serializers
from blog.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    auther = serializers.ReadOnlyField(source='auther.username')

    class Meta:
        model = BlogPost
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', '']