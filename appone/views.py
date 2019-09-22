from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from appone.forms import TestForm, LeaveComment
from appone.models import Post, NewPost, Dislikes, \
    Likesd, Dislikes_Author, Likes_Dislikes, Dislikes_Likes, \
    Likes_And_Dislikes, NewPost_Likes_Dislikes, LeaveAComment


class PostListView(ListView):
    model = NewPost_Likes_Dislikes
    template_name = 'appone/home.html'
    context_object_name = 'Post'


# def search(request, word=None):
#     # if request.method == "GET" and "search" in request.GET:
#     searching = NewPost_Likes_Dislikes.objects.filter(text__regex=word)
#     return render(request, 'appone/search.html', {"search": searching})

def search(request):
    if request.method == "GET":

        word = request.GET['q'].strip()
        print("WORD", word)
        searching = NewPost_Likes_Dislikes.objects.filter(text__regex=word)
        if searching:
            return render(request, 'appone/search.html', {"search": searching})

        return render(request, 'appone/search_empty.html', {})

@login_required
def form(request):

    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            song = NewPost_Likes_Dislikes(title=form.cleaned_data['title'],
                           text=form.cleaned_data['text'],
                           author=request.user.username)
            song.save()
            messages.success(request, 'Your post has been saved')
            return redirect('home')
    else:
        form = TestForm()

    return render(request, 'appone/index.html', {"form": form})


@login_required
def likes(request):

    if request.method == "POST" and "likes" in request.POST:
        o = Likesd(likes=0)
        o.save()
        like = Likesd.objects.get(pk=1).likes
        like +=1
        Likesd.objects.filter(pk=1).update(likes=like)

    elif request.method == "POST" and "dislikes" in request.POST:
        o = Dislikes(dislikes=0)
        o.save()
        like = Dislikes.objects.get(pk=1).dislikes
        like +=1
        Dislikes.objects.filter(pk=1).update(dislikes=like)

    elif request.method == "POST" and "dislikes_author" in request.POST:

        if Dislikes_Author.objects.filter(author=request.user.username).exists():
            like = Dislikes_Author.objects.get(author=request.user.username).dislikes
            like += 1
            Dislikes_Author.objects.filter(author=request.user.username).update(dislikes=like)

        elif not Dislikes_Author.objects.filter(author=request.user.username).exists():
            o = Dislikes_Author(author=request.user.username, dislikes=0)
            o.save()
            like = Dislikes_Author.objects.get(author=request.user.username).dislikes
            like +=1
            Dislikes_Author.objects.filter(author=request.user.username).update(dislikes=like)

        return redirect('http://localhost:8000')

    result = 0

    for s in Dislikes_Author.objects.all():
        result = result + s.dislikes

    return render(request, 'appone/likes.html',
                  {"likes": Likesd.objects.get(pk=1).likes,
                   "dislikes": Dislikes.objects.get(pk=1).dislikes,
                   "dislikes_author": result,
                   })


@login_required
def get_one_post_likes_dislikes(request, pk):
    template = loader.get_template('appone/one_post.html')

    if request.method == "POST" and "likes" in request.POST:

        if Likes_And_Dislikes.objects.filter(author=request.user.username, title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():
            like = Likes_And_Dislikes.objects.get(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).likes
            dislike = Likes_And_Dislikes.objects.get(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).dislikes
            if like == 1 and dislike == 0:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(likes=0)
            elif like == 0 and dislike == 1:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(dislikes=0)

            elif like == 0 and dislike == 0:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(likes=1)


        elif not Likes_And_Dislikes.objects.filter(author=request.user.username,
                                               title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():
            o = Likes_And_Dislikes(author=request.user.username,
                               title=NewPost_Likes_Dislikes.objects.get(pk=pk).title,
                               likes=0, dislikes=0)
            o.save()
            like = Likes_And_Dislikes.objects.get(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).likes

            Likes_And_Dislikes.objects.filter(author=request.user.username, title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(
                likes=1)

    if request.method == "POST" and "dislikes" in request.POST:

        if Likes_And_Dislikes.objects.filter(author=request.user.username, title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():
            like = Likes_And_Dislikes.objects.get(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).likes
            dislike = Likes_And_Dislikes.objects.get(author=request.user.username,
                                                 title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).dislikes
            if dislike == 1 and like == 0:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(dislikes=0)
            elif dislike == 0 and like == 1:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(likes=0)

            elif dislike == 0 and like == 0:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(dislikes=1)


        elif not Likes_And_Dislikes.objects.filter(author=request.user.username,
                                               title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():
            o = Likes_And_Dislikes(author=request.user.username,
                               title=NewPost_Likes_Dislikes.objects.get(pk=pk).title,
                               likes=0, dislikes=0)
            o.save()
            like = Likes_And_Dislikes.objects.get(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).dislikes

            Likes_And_Dislikes.objects.filter(author=request.user.username, title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(
                dislikes=1)

    if request.method == "POST" and "leave_comment" in request.POST:

        comment = LeaveComment(request.POST)
        if comment.is_valid():
            song = LeaveAComment(content=comment.cleaned_data['content'],
                                 title=NewPost_Likes_Dislikes.objects.get(pk=pk).title,
                                 author=request.user.username)
            song.save()
            messages.success(request, 'Your comment has been saved')

    else:
        comment = LeaveComment()

    test = LeaveAComment.objects.all().filter(title=NewPost_Likes_Dislikes.objects.get(pk=pk)).count()
    NewPost_Likes_Dislikes.objects.filter(pk=pk).update(number_comments=str(test))

    all_comments = ""

    for s in LeaveAComment.objects.all().filter(title=NewPost_Likes_Dislikes.objects.get(pk=pk).title):
        all_comments = all_comments + s.content

    likes = 0

    for s in Likes_And_Dislikes.objects.all().filter(title=NewPost_Likes_Dislikes.objects.get(pk=pk).title):
        likes = likes + s.likes

    NewPost_Likes_Dislikes.objects.filter(pk=pk).update(likes=likes)

    dislikes = 0

    for s in Likes_And_Dislikes.objects.all().filter(title=NewPost_Likes_Dislikes.objects.get(pk=pk).title):
        dislikes = dislikes + s.dislikes

    NewPost_Likes_Dislikes.objects.filter(pk=pk).update(dislikes=dislikes)

    context = {'title': NewPost_Likes_Dislikes.objects.get(pk=pk).title,
               'text': NewPost_Likes_Dislikes.objects.get(pk=pk).text,
               'author': NewPost_Likes_Dislikes.objects.get(pk=pk).author,
               "likes": likes,
               "dislikes": dislikes,
               "comment": comment,
               "all_comments": LeaveAComment.objects.order_by('-date_posted').all().filter(title=NewPost_Likes_Dislikes.objects.get(pk=pk).title),}

    return HttpResponse(template.render(context, request))


def test(request):

    return render(request, 'appone/test.html')
