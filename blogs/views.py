from django.shortcuts import render, redirect
from .forms import CreateUserFrom
from .models import Blog, Author
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_page(request):
    form = CreateUserFrom()
    if request.method == "POST":
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'User create successfull ' + username)
            return redirect('login')
    context = {"forms": form}
    return render(request, 'blogs/register.html',context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user.id)

            return redirect(f'home/{user}')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'blogs/login.html')


@login_required(login_url='login')
def home(request, pk):
    blogs = Blog.objects.all()
    author = Author.objects.get(name=pk)
    print(request.user.id)
    context = {
        'blog': blogs,
        'author': author
    }
    return render(request, 'blogs/main_body.html', context)
    

def home2(request, pk):
    current_blog = Blog.objects.get(id=pk)
    author = Author.objects.get(id=pk)
    print(current_blog)
    tag = current_blog.tags.all()
    tags = []
    for i in range(len(tag)):

        tags.append(tag[i])
    context = {
        'current': current_blog,
        'tags': tags,
        'author':author
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


def author_edit(request,pk):
    author = Author.objects.get(id=pk)
    context = {
        'author':author
    }
    return render(request,'blogs/author_edit.html', context)


def blog_write(request):
    if request.method == "GET":
        authors = Author.objects.all()

        context = {
            'aut': authors,

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

