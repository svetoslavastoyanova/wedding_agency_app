from django import forms

from djangoProject.add_post.models import MainPost
from djangoProject.comments.models import Comment


class AddCommentForm(forms.ModelForm):
    post_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('text', 'post_pk')

    def save(self, commit=True):
        post_pk = self.cleaned_data['post_pk']
        post = MainPost.objects.get(pk=post_pk)
        comment = Comment(
            text=self.cleaned_data['text'],
            post=post,

        )

        if commit:
            comment.save()

        return comment



