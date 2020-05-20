from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = ProcessedImageField(
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 90},
        upload_to='media',
        )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('HashTag', related_name="taged_post")

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    creted_at = models.DateField(auto_now_add=True)
    comment_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="comment_like_users")

class HashTag(models.Model):
    name = models.CharField(max_length=100)