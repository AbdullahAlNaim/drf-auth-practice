from blog.models import BlogPost
from blog.serializers import BlogPostSerializer, UserSerializer
from rest_framework import viewsets
from .permissions import permissions
from django.contrib.auth.models import User


# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_class = [permissions.IsauthenticatedOrReadOnly,
    IsownerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer