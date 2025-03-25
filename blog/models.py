from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='author_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    authors = models.ManyToManyField(Author, related_name="posts") 
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    time = models.DateTimeField(auto_now_add=True, null=True)
    ip = models.GenericIPAddressField(default=None, null=True)
    user_agent = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return str(self.name)