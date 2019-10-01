from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings

class Song(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    # test = RichTextField()

    def __str__(self):

        return "{} {}".format(self.name, self.age)

class Songo(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    # test = RichTextField()

    def __str__(self):

        return "{} {}".format(self.name, self.age)

class Songoa(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    test = RichTextField()

    def __str__(self):

        return "{} {}".format(self.name, self.age)

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class NewPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class NewPost_Likes_Dislikes(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=100)
    likes = models.CharField(max_length=100,default=0)
    dislikes = models.CharField(max_length=100, default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    number_comments = models.CharField(max_length=100,default=0)
    count = models.IntegerField(default=0)
    tags = models.CharField(max_length=200, default="Python")

    class Meta:
        ordering = ['-date_posted']


    def __str__(self):
        return self.title


class Likes(models.Model):
    title = models.CharField(default="toto",max_length=255)
    text = models.CharField(default="toto", max_length=255)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.pk


class Likesd(models.Model):
    title = models.CharField(default="toto",max_length=255)
    text = models.CharField(default="toto", max_length=255)
    likes = models.IntegerField(default=0)

class Dislikes(models.Model):
    title = models.CharField(default="toto",max_length=255)
    text = models.CharField(default="toto", max_length=255)
    dislikes = models.IntegerField(default=0)


class Dislikes_Author(models.Model):
    author = models.CharField(max_length=100)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.author


class Likes_Dislikes(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.author

class Dislikes_Likes(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.author


class Likes_And_Dislikes(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.author


class LeaveAComment(models.Model):
    # content = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

class Count(models.Model):
    count = models.IntegerField(default=0)

class Counts(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    count = models.IntegerField(default=0)

class TestList(models.Model):
    tags = models.CharField(max_length=200)