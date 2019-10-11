
from django.contrib import admin
from django.urls import path

from appone import views
from appone.views import PostListView

urlpatterns = [
    # path('', PostListView.as_view(), name="home"),
    path('', views.all_posts, name="home"),
    path('post', views.form, name="post"),
    path('search', views.search, name="search"),
    path('post/<int:pk>', views.get_one_post_likes_dislikes, name="postone"),
    path('tag/<str:tag>', views.tags, name="tag"),
    path('my_posts', views.my_posts, name="my_posts"),
    path('post/edit/<int:pk>', views.edit_a_post, name="edit_a_post"),
    path('post/delete/<int:pk>', views.delete_a_post, name="delete_a_post"),
    path('my_notifications', views.my_notifications, name="my_notifications"),
    path('my_notifications/view/<int:pk>', views.notification, name="notification"),

    path('test', views.test, name="test"),
    path('blog', views.blog, name="test"),
]
