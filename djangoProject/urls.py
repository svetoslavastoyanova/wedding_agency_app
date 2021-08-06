"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoProject.wedding.views import home, about_us, gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoProject.wedding.urls')),
    path('auth/', include('djangoProject.wedding_auth.urls')),
    path('profiles/', include('djangoProject.profiles.urls')),
    path('addpost/', include('djangoProject.add_post.urls')),
    path('comments/', include('djangoProject.comments.urls')),
    path('testimonials/', include('djangoProject.testimonials.urls')),


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

