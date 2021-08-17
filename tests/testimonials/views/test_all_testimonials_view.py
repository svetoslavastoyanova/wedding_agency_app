from django.urls import reverse
from tests.base.tests import WeddingTestCase


class AllTestimonialsViewTest(WeddingTestCase):
    def test_showAllTestimonialsForLoggedIn_andNotLoggedInUsers(self):
        response = self.client.get(reverse('show testimonials'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'testimonial/show-testimonials.html')
