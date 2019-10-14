from django.contrib import admin

from appone.models import Song, Post, \
    Likes, Dislikes, \
    Likes_Dislikes, Dislikes_Likes, Likes_And_Dislikes, \
    NewPost_Likes_Dislikes, LeaveAComment,\
    Count, Counts, LeaveACommentInComment, UserDetails

admin.site.register(Song)
admin.site.register(Post)

admin.site.register(NewPost_Likes_Dislikes)
admin.site.register(Likes)
admin.site.register(Dislikes)
admin.site.register(Likes_Dislikes)
admin.site.register(Dislikes_Likes)
admin.site.register(Likes_And_Dislikes)
admin.site.register(LeaveAComment)
admin.site.register(Count)
admin.site.register(Counts)
admin.site.register(LeaveACommentInComment)
admin.site.register(UserDetails)

