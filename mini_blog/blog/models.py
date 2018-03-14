from datetime import date
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Blogger(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True, blank = True)
    location = models.CharField(max_length = 200, null = True)
    bio = models.TextField(null = True , blank = True)

    def __str__(self):
        return "%s, %s"%self.first_name , self.last_name

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

class BlogPost(models.Model):
    blog_post_title = models.CharField(max_length = 200)
    post_date = models.DateField(null = True , default = date.today())
    blogger = models.ForeignKey(Blogger, on_delete = models.SET_NULL, null = True)
    content = models.TextField()
    
    def __str__(self):
        return self.blog_post_title

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    blog_post = models.ForeignKey(BlogPost, on_delete = models.SET_NULL , null = True)
    comment_date = models.DateField(default = date.today())
    comment_time = models.TimeField(default =timezone.now())
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text