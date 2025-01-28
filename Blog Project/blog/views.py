from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    
    # for adding a new Post
    post = Post()
    post.title = 'Why Python is Great for Web Development'
    post.content = 'Python is a versatile language that is great for web development, data analysis, artificial intelligence, and more!'
    post.author = 'Corey Schafer'
    post.save()

    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})