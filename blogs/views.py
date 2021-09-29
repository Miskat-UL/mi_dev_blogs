from django.shortcuts import render


def home(request):
    return render(request, 'blogs/index2.html')
    

def home2(request):
    return render(request, 'blogs/single_blog_page.html')
