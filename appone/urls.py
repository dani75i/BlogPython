
from django.contrib import admin
from django.urls import path

from appone import views
from appone.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post', views.form, name="post"),
    path('likes', views.likes, name="likes"),
    path('search/', views.search, name="search"),
    path('postone/<int:pk>', views.get_one_post_likes_dislikes, name="postone"),

    path('test', views.test, name="test")
]
