from django.contrib import admin

from appone.models import Song, Post, \
    NewPost, Likes, Likesd, Dislikes, Dislikes_Author, \
    Likes_Dislikes, Dislikes_Likes, Likes_And_Dislikes, \
    NewPost_Likes_Dislikes, LeaveAComment

admin.site.register(Song)
admin.site.register(Post)
admin.site.register(NewPost)
admin.site.register(NewPost_Likes_Dislikes)
admin.site.register(Likes)
admin.site.register(Likesd)
admin.site.register(Dislikes)
admin.site.register(Dislikes_Author)
admin.site.register(Likes_Dislikes)
admin.site.register(Dislikes_Likes)
admin.site.register(Likes_And_Dislikes)
admin.site.register(LeaveAComment)
