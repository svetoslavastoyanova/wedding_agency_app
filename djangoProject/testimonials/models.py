from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Testimonial(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='testimonials')
    testimony = models.TextField(max_length=120)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    testimonial = models.ForeignKey(Testimonial, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
