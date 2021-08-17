from django import forms
from djangoProject.core.validators import first_name_validator, last_name_validator, age_validator
from djangoProject.core.forms import BootstrapFormMixin
from djangoProject.profiles.models import Profile


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')

    first_name = forms.CharField(
        validators=[first_name_validator],
    )
    last_name = forms.CharField(
        validators=[last_name_validator],
    )

    age = forms.IntegerField(
        validators=[age_validator],
    )


