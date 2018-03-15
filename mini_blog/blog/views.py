from django.shortcuts import render
from django.views import generic
from .models import Blogger, BlogPost
# Create your views here.

def index(request):
    return render(request,
        'blog/index.html',
        context ={})

class AllBlogsListView(generic.ListView):
    model = BlogPost
    paginate_by = 5
    context_object_name= 'blog_list'
    template_name = 'blog/blog_list.html'
    def get_queryset(self):
        return BlogPost.objects.all().order_by('post_date')

class AllBloggersListView(generic.ListView):
    model = Blogger
    paginate_by = 10
    context_object_name = 'blogger_list'
    template_name = 'blog/blogger_list.html'

    def get_queryset(self):
        return Blogger.objects.all()

def blog_detail(request , pk):
    pass

def blogger_detail(request , pk):
    pass
    

