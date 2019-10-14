from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from appone.models import NewPost_Likes_Dislikes
from users.forms import UserCreationFormCustom, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account created for {}".format(username))
            return redirect('login')
    else:
        form = UserCreationFormCustom()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    form = "ok"

    notifications = 0

    for s in NewPost_Likes_Dislikes.objects.all(). \
            filter(author=request.user.username):
        notifications = notifications + s.notifications

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=request.user)


    return render(request, 'users/profile.html', {
        'form': form,
        "update_form": u_form,
        "Notifications": notifications,
    })
