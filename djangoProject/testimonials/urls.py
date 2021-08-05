from django.urls import path

from djangoProject.testimonials.views import show_testimonials, testimony_details, like_testimony, create_testimony, \
    edit_testimony, delete_testimony

urlpatterns = (
    path('', show_testimonials, name='show testimonials'),
    path('details/<int:pk>', testimony_details, name='testimony details'),
    path('like/<int:pk>', like_testimony, name='like testimony'),
    path('create/', create_testimony, name='create testimony'),
    path('edit/<int:pk>', edit_testimony, name='edit testimony'),
    path('delete/<int:pk>', delete_testimony, name='delete testimony'),

)