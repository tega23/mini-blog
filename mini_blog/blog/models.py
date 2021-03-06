from datetime import date
from django.db import models
from datetime import time
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Blogger(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 50)
    date_of_birth = models.DateField(null = True, blank = True)
    location = models.CharField(max_length = 200, null = True)
    bio = models.TextField(null = True , blank = True)

    def __str__(self):
        return "{}".format(self.username)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

class BlogPost(models.Model):
    blog_post_title = models.CharField(max_length = 400)
    post_date = models.DateField(null = True , default = timezone.now)
    post_time = models.TimeField(null = True , default = timezone.now)
    blogger = models.ForeignKey(Blogger, on_delete = models.SET_NULL, null = True)
    content = models.TextField()

    class Meta:
        ordering = ['-post_date', '-post_time']

    def __str__(self):
        return "{}".format(self.blog_post_title)
    

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    blog_post = models.ForeignKey(BlogPost, on_delete = models.SET_NULL , null = True)
    comment_date = models.DateField(default = timezone.now)
    comment_time = models.TimeField(default = timezone.now)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text