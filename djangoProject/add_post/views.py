
from django.shortcuts import render, redirect

from djangoProject.add_post.forms import MainPostForm
from djangoProject.add_post.models import MainPost


def add_main_post(request):
    form = MainPostForm()

    if request.method == 'POST':
        form = MainPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show main post')
    else:
        form = MainPostForm()

    context = {
        "form": form
    }

    return render(request, 'add_post/add-mainpost.html', context)


def show_main_post(request):
    post = MainPost.objects.all()

    context = {
        'post': post,
    }
    return render(request, 'add_post/show_main_post.html', context)
