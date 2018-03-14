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
    context_name = 'blog_list'
    template_name = 'blog_list.html'
    def get_queryset(self):
        return BlogPost.objects.all().order_by(post_date)

class AllBloggersListView(generic.ListView):
    model = Blogger
    paginate_by = 10

    def get_queryset(self):
        return Blogger.objects.all()

