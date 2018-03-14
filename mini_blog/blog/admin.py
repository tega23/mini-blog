from django.contrib import admin
from .models import Blogger, Comment, BlogPost

# Register your models here.

admin.site.register(Blogger)
admin.site.register(Comment)
admin.site.register(BlogPost)

