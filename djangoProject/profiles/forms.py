from django import forms

from djangoProject.core.forms import BootstrapFormMixin
from djangoProject.profiles.models import Profile


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')