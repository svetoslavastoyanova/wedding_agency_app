from django.urls import reverse
from djangoProject.comments.models import Comment
from tests.base.utils import UserTestUtils, PostTestUtils
from tests.base.tests import WeddingTestCase


class PostDetailsTest(PostTestUtils, UserTestUtils, WeddingTestCase):
    def test_getPostDetailsForAllUsers(self):
        self.client.force_login(self.user)
        post = self.create_post(
            image='path/to/image.png',
        )

        response = self.client.get(reverse('post to comment', kwargs={
            'pk': post.id,
        }))

        self.assertTrue(response.context['post'])

    def test_commentPostForLoggedInUser(self):
        self.client.force_login(self.user)
        comment_user = self.create_user(email='testimony@user.com', password='asdfgh')
        post = self.create_post_with_comment(
            comment_user=self.user,
            image='path/to/image.png',
        )

        response = self.client.post(reverse('add comment', kwargs={
            'pk': post.id,
        }))

        self.assertEqual(302, response.status_code)

        comment_exists = Comment.objects.filter(

            user_id=self.user.id,
            post_id=post.id,
        ) \
            .exists()

        self.assertTrue(comment_exists)