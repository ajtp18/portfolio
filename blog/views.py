from django.shortcuts import render, get_object_or_404

from blog.models import Post

# Create your views here.

def render_posts(requests):
    posts = Post.objects.all()
    return render(requests, 'posts.html', {'posts':posts})

def post_details(requests, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(requests, 'post_details.html', {"post":post})