from datetime import date
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.


def index(request):

    latest = Post.objects.order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        "posts": latest
    })


def posts(request):
    all_posts = Post.objects.all()

    return render(request, 'blog/all-posts.html', {
        "posts": all_posts
    })


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {"post": post})
