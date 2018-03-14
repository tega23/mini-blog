from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('blogs/', views.AllBlogsListView.as_view(), name ='all-blogs'),
    path('bloggers/', views.AllBloggersListView.as_view(), name ='all-bloggers'),
]