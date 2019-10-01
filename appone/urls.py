
from django.contrib import admin
from django.urls import path

from appone import views
from appone.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post', views.form, name="post"),
    path('search', views.search, name="search"),
    path('post/<int:pk>', views.get_one_post_likes_dislikes, name="postone"),
    path('tag/<str:tag>', views.tags, name="tag"),

    path('test', views.test, name="test"),
    path('blog', views.blog, name="test"),
]
