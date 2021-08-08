from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from djangoProject.testimonials.forms import TestimonialForm, EditTestimonyForm
from djangoProject.testimonials.models import Testimonial, Like


def show_testimonials(request):
    all_testimonials = Testimonial.objects.all()
    context = {
        'testimonials': all_testimonials,
    }

    return render(request, 'testimonial/show-testimonials.html', context)


def testimony_details(request, pk):
    testimonial = Testimonial.objects.get(pk=pk)
    testimonial.likes_count = testimonial.like_set.count()

    is_user = testimonial.user == request.user

    context = {
        'testimonial': testimonial,
        'is_user': is_user,
    }

    return render(request, 'testimonial/testimonial-detail.html', context)


@login_required(login_url='sign in')
def like_testimony(request, pk):
    testimonial = Testimonial.objects.get(pk=pk)
    like_object_by_user = testimonial.like_set.filter(user_id=request.user.id) \
        .first()
    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            testimonial=testimonial,
            user=request.user,
        )
        like.save()
    return redirect('testimony details', testimonial.id)


def create_testimony(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimony = form.save(commit=False)
            testimony.user = request.user
            testimony.save()
            return redirect('show testimonials')
    else:
        form = TestimonialForm()

    context = {
        'form': form,
    }

    return render(request, 'testimonial/create-testimonial.html', context)


def edit_testimony(request, pk):
    testimony = Testimonial.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditTestimonyForm(request.POST, request.FILES, instance=testimony)
        if form.is_valid():
            form.save()
            return redirect('show testimonials')
    else:
        form = EditTestimonyForm(instance=testimony)

    context = {
        'form': form,
        'testimony': testimony,
    }

    return render(request, 'testimonial/testimonial_edit.html', context)


def delete_testimony(request, pk):
    testimony = Testimonial.objects.get(pk=pk)
    if request.method == 'POST':
        testimony.delete()
        return redirect('show testimonials')
    else:
        context = {
            'testimony': testimony,
        }
        return render(request, 'testimonial/delete-testimonial.html', context)