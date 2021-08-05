from django.urls import path

from djangoProject.add_post.views import show_main_post
from djangoProject.comments.views import post_to_comment, add_comment

urlpatterns = (
    path('', show_main_post, name='show main post'),
    path('show/<int:pk>', post_to_comment, name='post to comment'),
    path('comment/<int:pk>', add_comment, name='add comment'),



)