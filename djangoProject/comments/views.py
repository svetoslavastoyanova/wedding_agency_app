from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from djangoProject.add_post.models import MainPost
from djangoProject.comments.forms import AddCommentForm
from django.views.generic.edit import UpdateView, DeleteView

from djangoProject.comments.models import Comment


def post_to_comment(request, pk):
    post = MainPost.objects.get(pk=pk)

    context = {
        'post': post,
        'comment_form': AddCommentForm(
            initial={
                'post_pk': pk,
            }
        ),
        'comments': post.comment_set.all(),
    }
    return render(request, 'comments/post_to_comment.html', context)


def add_comment(request, pk):
    form = AddCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('post to comment', pk)




