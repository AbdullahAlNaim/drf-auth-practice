from blog.models import BlogPost
from blog.serializers import BlogPostSerializer, UserSerializer
from rest_framework import viewsets, mixins
from rest_framework import permissions
from .permissions import IsOwnerReadOnly
from django.contrib.auth.models import User


# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()

        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(author=user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    
class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.AllowAny,]

    