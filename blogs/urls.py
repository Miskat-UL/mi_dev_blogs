from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.home, name="home"),
    path('news/<int:pk>', views.home2, name='news'),
    path('likes/<int:pk>', views.get_likes, name='likes'),
    path('author/<int:pk>', views.home3 ,name='author'),
]
