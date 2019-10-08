from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from appone.forms import TestForm, LeaveComment
from appone.models import Post, NewPost, Dislikes, \
    Dislikes_Author, Likes_Dislikes, Dislikes_Likes, \
    Likes_And_Dislikes, NewPost_Likes_Dislikes, LeaveAComment, Counts


class PostListView(ListView):
    model = NewPost_Likes_Dislikes
    template_name = 'appone/all_posts.html'
    context_object_name = 'Post'


def search(request):
    if request.method == "GET":

        word = request.GET['q'].strip()
        print("WORD", word)
        searching = NewPost_Likes_Dislikes.objects.filter(text__regex=word)
        if searching:
            return render(request, 'appone/search.html', {"search": searching})

        return render(request, 'appone/search_empty.html', {})


def tags(request, tag):
    search_tag = NewPost_Likes_Dislikes.objects.filter(tags__regex=tag)
    return render(request, 'appone/search_tag.html', {
        "search_tag": search_tag,
        "tag": tag
    })


@login_required
def form(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            song = NewPost_Likes_Dislikes(title=form.cleaned_data['title'],
                                          tags=form.cleaned_data['tags'],
                                          text=form.cleaned_data['text'],
                                          author=request.user.username)
            song.save()
            messages.success(request, 'Your post has been saved')
            return redirect('home')
    else:
        form = TestForm()

    return render(request, 'appone/add_post.html', {"form": form})


# @login_required
def get_one_post_likes_dislikes(request, pk):
    template = loader.get_template('appone/one_post.html')

    if request.method == "GET":
        if Counts.objects.filter(author=request.user.username,
                                 title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():

            count = Counts.objects.get(author=request.user.username,
                                       title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).count

            if count == 0:
                Counts.objects.filter(author=request.user.username,
                                      title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(count=1)

        elif not Counts.objects.filter(author=request.user.username,
                                       title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():

            o = Counts(author=request.user.username,
                       title=NewPost_Likes_Dislikes.objects.get(pk=pk).title,
                       count=0)
            o.save()

    views = 0

    for s in Counts.objects.all().filter(title=NewPost_Likes_Dislikes.objects.get(pk=pk).title):
        views = views + s.count

    NewPost_Likes_Dislikes.objects.filter(pk=pk).update(count=views)

    if request.method == "POST" and "likes" in request.POST:

        if Likes_And_Dislikes.objects.filter(author=request.user.username,
                                             title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():
            like = Likes_And_Dislikes.objects.get(author=request.user.username,
                                                  title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).likes
            dislike = Likes_And_Dislikes.objects.get(author=request.user.username,
                                                     title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).dislikes
            if like == 1 and dislike == 0:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                                  title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(likes=0)
            elif like == 0 and dislike == 1:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                                  title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(
                    dislikes=0)

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

            Likes_And_Dislikes.objects.filter(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(
                likes=1)

    if request.method == "POST" and "dislikes" in request.POST:

        if Likes_And_Dislikes.objects.filter(author=request.user.username,
                                             title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():
            like = Likes_And_Dislikes.objects.get(author=request.user.username,
                                                  title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).likes
            dislike = Likes_And_Dislikes.objects.get(author=request.user.username,
                                                     title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).dislikes
            if dislike == 1 and like == 0:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                                  title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(
                    dislikes=0)
            elif dislike == 0 and like == 1:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                                  title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(likes=0)

            elif dislike == 0 and like == 0:
                Likes_And_Dislikes.objects.filter(author=request.user.username,
                                                  title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(
                    dislikes=1)


        elif not Likes_And_Dislikes.objects.filter(author=request.user.username,
                                                   title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).exists():
            o = Likes_And_Dislikes(author=request.user.username,
                                   title=NewPost_Likes_Dislikes.objects.get(pk=pk).title,
                                   likes=0, dislikes=0)
            o.save()
            like = Likes_And_Dislikes.objects.get(author=request.user.username,
                                                  title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).dislikes

            Likes_And_Dislikes.objects.filter(author=request.user.username,
                                              title=NewPost_Likes_Dislikes.objects.get(pk=pk).title).update(
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

    ############################
    # BEGIN REPLY TO A COMMENT #
    ############################

    ##########################
    # END REPLY TO A COMMENT #
    ##########################

    likes = 0

    for s in Likes_And_Dislikes.objects.all().filter(title=NewPost_Likes_Dislikes.objects.get(pk=pk).title):
        likes = likes + s.likes

    NewPost_Likes_Dislikes.objects.filter(pk=pk).update(likes=likes)

    dislikes = 0

    for s in Likes_And_Dislikes.objects.all().filter(title=NewPost_Likes_Dislikes.objects.get(pk=pk).title):
        dislikes = dislikes + s.dislikes

    NewPost_Likes_Dislikes.objects.filter(pk=pk).update(dislikes=dislikes)

    context = {
        'title': NewPost_Likes_Dislikes.objects.get(pk=pk).title,
        'text': NewPost_Likes_Dislikes.objects.get(pk=pk).text,
        'author': NewPost_Likes_Dislikes.objects.get(pk=pk).author,
        'date_posted': NewPost_Likes_Dislikes.objects.get(pk=pk).date_posted,
        'number_comments': NewPost_Likes_Dislikes.objects.get(pk=pk).number_comments,
        "likes": likes,
        "dislikes": dislikes,
        "comment": comment,
        "all_comments": LeaveAComment.objects.order_by('date_posted').all().filter(
            title=NewPost_Likes_Dislikes.objects.get(pk=pk).title),
        "count": views,
    }

    return HttpResponse(template.render(context, request))


def test(request):
    # if request.method == "GET":
    #     count = Count.objects.get(pk=1).count
    #     print("BEFORE : ", count)
    #     count = count + 1
    #     count = Count.objects.filter(pk=1).update(count=count)
    #     print("AFTER : ", count)
    #     count = Count.objects.get(pk=1).count

    return render(request, 'appone/test.html', {})


def blog(request):
    return render(request, 'appone/all_posts.html')


@login_required
def my_posts(request):

    my_posts = NewPost_Likes_Dislikes.objects.filter(author=request.user.username)
    return render(request, 'appone/my_posts.html', {
        "my_posts": my_posts,
    })

@login_required
def edit_a_post(request, pk):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            NewPost_Likes_Dislikes.objects.filter(pk=pk).update(
                title=form.cleaned_data['title'],
                tags=form.cleaned_data['tags'],
                text=form.cleaned_data['text'],
                author=request.user.username)
            messages.success(request, 'Your comment has been updated')
            return redirect('my_posts')

    else:
        form = TestForm()

    return render(request, 'appone/edit_post.html', {
        "form": form,
    })


@login_required
def delete_a_post(request, pk):
    NewPost_Likes_Dislikes.objects.filter(pk=pk).delete()
    messages.warning(request, 'Your comment has been deleted')
    return redirect('my_posts')