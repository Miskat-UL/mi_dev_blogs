from django.shortcuts import render
from .models import Blog


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blog': blogs
    }
    return render(request, 'blogs/index2.html', context)
    

def home2(request, pk):
    current_blog = Blog.objects.get(id=pk)
    context = {
        'current': current_blog
    }
    return render(request, 'blogs/single_blog_page.html', context)
