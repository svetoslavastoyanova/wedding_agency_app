from django.urls import reverse

from tests.base.tests import WeddingTestCase


class SignInViewTest(WeddingTestCase):
    def test_signInSuccess_shouldRedirectToHome(self):
        response = self.client.post(reverse('sign in'), data={'username': 'amm@abv.bg', 'password': 'asdfgh'})
        self.assertEqual(302, response.status_code)
        self.assertEqual('/', response.headers['location'])

    def test_wrong_username(self):
        response = self.client.post(reverse('sign in'), {'username': 'wrong', 'password': 'asdfgh'})
        self.assertEqual(200, response.status_code)
        errors = response.context_data['form'].errors['password']
        default_error = 'Please enter a correct email and password. Note that both fields may be case-sensitive.'
        self.assertIn(default_error, errors)

    def test_wrong_password(self):
        response = self.client.post(reverse('sign in'), {'username': 'amm@abv.bg', 'password': 'wrong'})
        self.assertEqual(200, response.status_code)
        errors = response.context_data['form'].errors['password']
        default_error = 'Please enter a correct email and password. Note that both fields may be case-sensitive.'
        self.assertIn(default_error, errors)