from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from djangoProject.profiles.forms import ProfileForm
from djangoProject.profiles.models import Profile
from djangoProject.testimonials.models import Testimonial


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    user_testimonials = Testimonial.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'profile': profile,
        'testimonials': user_testimonials,
    }

    return render(request, 'profiles/details.html', context)