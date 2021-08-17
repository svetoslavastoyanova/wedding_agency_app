
from django.urls import reverse
from tests.base.utils import TestimonialTestUtils, UserTestUtils
from tests.base.tests import WeddingTestCase


class TestimonialDetailsTest(TestimonialTestUtils, UserTestUtils, WeddingTestCase):
    def test_getTestimonyDetails_whenTestimonyExistsAndItsUser_shouldReturnDetailsForUser(self):
        self.client.force_login(self.user)
        testimony = self.create_testimony(
            title='Test Testimony',
            testimony='Test actual testimony',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('testimony details', kwargs={
            'pk': testimony.id,
        }))

        self.assertTrue(response.context['is_user'])

    def test_getTestimonyDetails_whenTestimonyExistsAndItsNotUser_shouldReturnDetailsForUser(self):
        self.client.force_login(self.user)
        new_user = self.create_user(email='testimony@user.com', password='asdfgh')
        testimony = self.create_testimony(
            title='Test Testimony',
            testimony='Test actual testimony',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('testimony details', kwargs={
            'pk': testimony.id,
        }))

        self.assertTrue(response.context['is_user'])