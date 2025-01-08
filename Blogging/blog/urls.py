from django.contrib import admin
from django.urls import path, include
from blog import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blog', views.BlogPostViewSet, basename='blog')
router.register(r'user', views.UserViewSet, basename='user')

urlpatterns = [
    # path('', include('blog.urls')),
    path('', include(router.urls))
]
