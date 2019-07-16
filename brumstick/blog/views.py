from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def home(request):
    blog_posts = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', blog_posts)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/model>_<viewtype>.html
    context_object_name = 'posts'    # define to match post object name above

class PostDetailView(DetailView):
    model = Post

def post(request):
    return render(request, 'blog/post.html')