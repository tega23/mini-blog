from django.shortcuts import render
from django.views import generic
# Create your views here.

def index(request):
    return render(request,
        'blog/index.html',
        context ={})

class AllBlogListView(generic.ListView):
    model = BlogPost
    paginate_by = 10

    def get_queryset(self):
        pass
class AllBloggersListView(generic.ListView):
    model = Blogger
    paginate_by = 10

    def get_queryset(self):
        pass

