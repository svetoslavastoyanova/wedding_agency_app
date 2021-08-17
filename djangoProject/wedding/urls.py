from django.urls import path
from djangoProject.wedding.views import home, about_us, gallery, prices

urlpatterns = (
    path('', home, name='home'),
    path('about/', about_us, name='about us'),
    path('gallery/', gallery,  name='gallery'),
    path('prices/', prices, name='prices'),
)