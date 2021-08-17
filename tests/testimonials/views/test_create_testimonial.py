from django.urls import reverse

from djangoProject.testimonials.models import Testimonial
from tests.base.tests import WeddingTestCase


class CreateTestimonialViewTest(WeddingTestCase):
    def test_createTestimonial_whenLoggedInUser_shouldRenderTemplate(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create testimony'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'testimonial/create-testimonial.html')

    def test_createTestimonyPost_shouldCreateTestimonial(self):
        self.client.force_login(self.user)
        self.client.post(
            reverse('create testimony'),
            data={
                'title': 'My day',
                'testimony': 'The best day in my life',
                'image': 'path/to/image.png',
                'user': self.user,
            }
        )
        user_testimonials = Testimonial.objects.filter()
        self.assertNotEqual(0, user_testimonials)