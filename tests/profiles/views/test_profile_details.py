from django.contrib.auth import get_user_model
from django.urls import reverse
from djangoProject.testimonials.models import Testimonial
from tests.base.tests import WeddingTestCase

UserModel = get_user_model()


class ProfileDetailsTest(WeddingTestCase):
    def test_getDetailsForLoggedInUserWithNoTestimonials(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['testimonials']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetailsForLoggedInUserWithTestimonials(self):
        testimonial = Testimonial.objects.create(
            title='Test Testimonial',
            testimony='Test actual testimony',
            image='path/to/image.png',
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([testimonial], list(response.context['testimonials']))





