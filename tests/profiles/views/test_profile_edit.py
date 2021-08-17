import random
from os.path import join
from django.conf import settings

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from djangoProject.profiles.models import Profile
from djangoProject.testimonials.models import Testimonial
from tests.base.tests import WeddingTestCase




class ProfileEditTest(WeddingTestCase):
    def test_postDetails_whenLoggedInUserWithNoPictureChangesImage(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_image.jpg')

        file_name = f'{random.randint(1, 10000)}-test_image.jpg'
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
        )

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': file,
        })

        self.assertEqual(200, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)

    def test_postDetails_whenLoggedInUserWithPictureChangesImage(self):
        path_to_image = 'path/to/image.png'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(200, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
