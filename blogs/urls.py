from django.urls import path
from blogs import views

urlpatterns = [
    path('home/<str:pk>', views.home, name="home"),
    path('news/<int:pk>', views.home2, name='news'),
    path('likes/<int:pk>', views.get_likes, name='likes'),
    path('author/<int:pk>', views.home3, name='author'),
    path('write_blog', views.blog_write, name="blog_create"),
    path('login', views.login_page, name="login"),
    path('register', views.register_page, name="register"),
    path('author_edit/<int:pk>', views.author_edit, name="author_edit"),
]
