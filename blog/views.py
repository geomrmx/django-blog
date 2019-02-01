from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'title': "Django blog", 'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})