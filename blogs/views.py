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
    tag = current_blog.tags.all()
    tags = []
    for i in range(len(tag)):

        tags.append(tag[i])
    context = {
        'current': current_blog,
        'tags': tags
    }
    return render(request, 'blogs/single_blog_page.html', context)
