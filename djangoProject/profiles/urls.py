from django.urls import path

from djangoProject.profiles.views import profile_details

urlpatterns = (
    path('', profile_details, name='profile details'),
)


import djangoProject.profiles.signals