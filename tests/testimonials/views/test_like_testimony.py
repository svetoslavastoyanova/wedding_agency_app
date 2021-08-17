from djangoProject.testimonials.models import Like
from tests.base.tests import WeddingTestCase
from django.urls import reverse
from tests.base.utils import TestimonialTestUtils, UserTestUtils


class LikeTestimonyViewTests(TestimonialTestUtils, UserTestUtils, WeddingTestCase):
    def test_likeTestimony_whenTestimonyNotLiked_shouldCreateLike(self):
        self.client.force_login(self.user)
        testimony_user = self.create_user(email='testimony@user.com', password='asdfgh')
        testimony = self.create_testimony(
            title='Test Testimony',
            testimony='Test actual testimony',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(reverse('like testimony', kwargs={
            'pk': testimony.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            testimonial_id=testimony.id,
        ) \
            .exists()

        self.assertTrue(like_exists)


    def test_likeTestimony_whenTestimonyIsLiked_shouldDeleteLike(self):
        self.client.force_login(self.user)
        testimony_user = self.create_user(email='testimony@user.com', password='asdfgh')
        testimony = self.create_testimony_with_like(
            like_user=self.user,
            title='Test Testimony',
            testimony='Test actual testimony',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(reverse('like testimony', kwargs={
            'pk': testimony.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            testimonial_id=testimony.id,
        ) \
            .exists()

        self.assertFalse(like_exists)
