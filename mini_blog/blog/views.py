from django.shortcuts import render,HttpResponseRedirect
from django.views import generic
from .models import Blogger, BlogPost , Comment
from .forms import UserCommentForm
from django.urls import reverse
from django.utils import timezone
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
    blogPost = BlogPost.objects.get(pk = pk)
    comment = Comment.objects.filter(blog_post__blogger__id =pk)
    if request.method == 'POST':
        form = UserCommentForm(data = request.POST)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            
            comment_ = form.cleaned_data['comment_text']
            new_comment  = Comment.objects.create(user = request.user, blog_post = blogPost , comment_text = comment_  )
            new_comment.save()
            previous_page_url = request.POST.get('next', '/')
            return HttpResponseRedirect(previous_page_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserCommentForm()
    return render (request,'blog/blog_detail.html',context ={'blog_post':blogPost, 'comment':comment , 'form':form})

def blogger_detail(request , pk):
    blogger = Blogger.objects.get(pk = pk)
    blog_posts =  BlogPost.objects.filter(blogger__id = pk)
    return render (request,
    'blog/blogger_detail.html',
    context ={'blogger': blogger, 'blog_posts':blog_posts},
    )


