from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.home, name="home"),
    path('news/<int:pk>', views.home2, name='news'),
    path('likes/<int:pk>', views.get_likes, name='likes'),
    path('write_blog/', views.blog_write, name="blog_create")
]
