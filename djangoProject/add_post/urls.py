from django.urls import path

from djangoProject.add_post.views import add_main_post, show_main_post


urlpatterns = (
    path('', add_main_post, name='add main post'),


)