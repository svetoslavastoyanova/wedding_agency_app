from django.urls import reverse
from tests.base.utils import UserTestUtils, TestimonialTestUtils
from tests.base.tests import WeddingTestCase


class TestimonialEditTest(TestimonialTestUtils, UserTestUtils, WeddingTestCase):
    def test_postTestimonyEditByItsUser(self):
        self.client.force_login(self.user)
        testimony = self.create_testimony(
            title='My wedding',
            testimony='The best day',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(
            reverse('edit testimony', kwargs={'pk': testimony.id}),
            {'title': 'New title', 'testimony': 'Nice'})

        self.assertEqual(response.status_code, 302)

        testimony.refresh_from_db()
        self.assertEqual(testimony.title, 'New title')