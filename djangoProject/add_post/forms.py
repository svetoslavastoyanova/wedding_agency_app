from django import forms


from djangoProject.add_post.models import MainPost


class MainPostForm(forms.ModelForm):
    class Meta:
        model = MainPost
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'image': 'Select an image: ',
        }