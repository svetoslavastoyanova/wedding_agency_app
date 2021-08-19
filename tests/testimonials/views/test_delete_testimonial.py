from django.urls import reverse
from tests.base.tests import WeddingTestCase
from tests.base.utils import TestimonialTestUtils


class DeleteTestimonialViewTest(WeddingTestCase, TestimonialTestUtils):
    def test_deleteTestimonial_whenLoggedInUser_shouldDeleteTestimonial(self):
        self.client.force_login(self.user)
        testimony = self.create_testimony(
            title='My wedding',
            testimony='The best day',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(reverse('delete testimony', kwargs={'pk': testimony.id}),)
        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, reverse('show testimonials'))

