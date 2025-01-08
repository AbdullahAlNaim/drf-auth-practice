from django.db import models

# Create your models here.
class BlogPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey('auth.User', related_name='blog', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']