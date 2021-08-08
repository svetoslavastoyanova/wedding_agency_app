from django.contrib.auth import get_user_model
from djangoProject.add_post.models import MainPost
from djangoProject.comments.models import Comment
from djangoProject.testimonials.models import Like, Testimonial

UserModel = get_user_model()


class TestimonialTestUtils:
    def create_testimony(self, **kwargs):
        return Testimonial.objects.create(**kwargs)

    def create_testimony_with_like(self, like_user, **kwargs):
        testimony = self.create_testimony(**kwargs)
        Like.objects.create(
            testimonial=testimony,
            user=like_user,
        )
        return testimony


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)


class PostTestUtils:
    def create_post(self, **kwargs):
        return MainPost.objects.create(**kwargs)

    def create_post_with_comment(self, comment_user, **kwargs):
        post = self.create_post(**kwargs)
        Comment.objects.create(
            post=post,
            user=comment_user,
        )
        return post

