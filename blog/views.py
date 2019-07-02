from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.


def all_posts(request):
    posts_list = Post.objects

    return render(request,'blog/blog.html',{'posts_list':posts_list} )


def detail(request, blog_id):
    post = get_object_or_404(Post,pk=blog_id)
    return render(request, 'blog/detail.html', {'post':post})