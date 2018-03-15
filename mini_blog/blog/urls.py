from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('blog/<int:pk>', views.blog_detail, name ='blog-detail'),
    path('blogs/', views.AllBlogsListView.as_view(), name ='all-blogs'),
    path('blogger/<int:pk>', views.blogger_detail, name ='blogger-detail'),
    path('bloggers/', views.AllBloggersListView.as_view(), name ='all-bloggers'),
]