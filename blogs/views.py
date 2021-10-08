from django.shortcuts import render, redirect
from .models import Blog,Author


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


def home3(request, pk):
    author = Author.objects.get(id=pk)
    # author = current_blog.author
    author_blog = Blog.objects.filter(author=author)

    context = {
        'author': author,
        'aut': author_blog
    }
    return render(request, 'blogs/author_page.html', context)


def get_likes(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.react += 1
    blog.save()
    return redirect('/')


def blog_write(request):
    if request.method == "GET":
        authors = Author.objects.all()
        context = {
            'aut': authors
        }

        return render(request, 'blogs/blogWrite.html', context)
    if request.method == "POST":
        blog = request.POST['editordata']
        title = request.POST['title']
        author = request.POST['author']
        b = Blog.objects.create(title=title, body=blog)
        b.author_id = author
        b.save()

        return redirect('/')

