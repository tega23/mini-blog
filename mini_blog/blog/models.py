from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date
# Create your models here.
class Blogger(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True, blank = True)
    location = models.CharField(max_length = 200, null = True)
    bio = models.TextField(null = True , blank = True)

class BlogPost(models.Model):
    blog_post_title = models.CharField(max_length = 200)
    post_date = models.DateField(null = True , default = date.today())
    blogger = models.ForeignKey(Blogger, on_delete = models.SET_NULL, null = True)
    content = models.TextField()
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    blog_post = models.ForeignKey(BlogPost, on_delete = models.SET_NULL , null = True)
    comment_date = models.DateField(default = date.today())
    comment_time = models.TimeField(default = datetime.now())
    comment_text = models.TextField()

