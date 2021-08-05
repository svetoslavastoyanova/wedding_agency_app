from django.contrib.auth import get_user_model
from django.db import models

from djangoProject.add_post.models import MainPost
UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(MainPost, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )