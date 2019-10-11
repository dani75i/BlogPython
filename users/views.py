from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from appone.models import NewPost_Likes_Dislikes


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account created for {}".format(username))
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    form = "ok"

    notifications = 0

    for s in NewPost_Likes_Dislikes.objects.all(). \
            filter(author=request.user.username):
        notifications = notifications + s.notifications


    return render(request, 'users/profile.html', {
        'form': form,
        "Notifications": notifications,
    })
