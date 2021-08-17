from django.urls import reverse

from tests.base.tests import WeddingTestCase


class SignOutViewTest(WeddingTestCase):
    def test_signOutSuccess_shouldRedirectToIndex(self):
        is_logged_in = self.client.login(username=self.logged_in_user_email, password=self.logged_in_user_password)
        self.assertTrue(is_logged_in)
        response = self.client.get(reverse('sign out'), follow=False)
        self.assertEqual(302, response.status_code)
        self.assertEqual(reverse('home'), response.headers['location'])