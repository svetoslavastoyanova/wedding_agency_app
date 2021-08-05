from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def about_us(request):
    return render(request, 'about-us.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})