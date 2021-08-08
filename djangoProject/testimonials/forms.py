import os
from os.path import join
from djangoProject.core.validators import first_letter_validator
from django import forms
from django.conf import settings

from djangoProject.core.forms import BootstrapFormMixin
from djangoProject.testimonials.models import Testimonial


class TestimonialForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Testimonial
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            ),
        }
    title = forms.CharField(
        validators=[first_letter_validator],
    )


class EditTestimonyForm(TestimonialForm):
    def save(self, commit=True):
        db_testimony = Testimonial.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_testimony.image))
            #os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Testimonial
        exclude = ('user',)
