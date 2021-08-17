from django.urls import reverse
from djangoProject.wedding_auth.forms import SignUpForm
from tests.base.tests import WeddingTestCase


class SignUpViewTest(WeddingTestCase):
    def test_getSignUp_shouldRenderTemplateAndForm(self):
        response = self.client.get(reverse('sign up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='auth/sign-up.html')
        self.assertIsInstance(response.context_data['form'], SignUpForm)


