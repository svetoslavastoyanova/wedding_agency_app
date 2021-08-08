from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from djangoProject.add_post.models import MainPost
from djangoProject.comments.forms import AddCommentForm


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


@login_required(login_url='sign in')
def add_comment(request, pk):
    form = AddCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('post to comment', pk)






