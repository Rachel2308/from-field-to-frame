from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Furniture
from .forms import FurnitureForm


def all_furniture(request):
    """View to return the furniture home page"""

    furniture = Furniture.objects.all()

    context = {
        'furniture': furniture,
    }

    return render(request, 'furniture/furniture.html', context)


def furniture_detail(request, furniture_id):
    """View to return the furniture detail page"""

    furniture = get_object_or_404(Furniture, pk=furniture_id)

    context = {
        'furniture': furniture,
    }

    return render(request, 'furniture/furniture_detail.html', context)


@login_required
def add_furniture(request):
    """Add furniture example to store"""
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have'
                       'permission to perform this function.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES)
        if form.is_valid():
            furniture = form.save()
            messages.success(request, 'Item added!')
            return redirect(reverse('furniture_detail', args=[furniture.id]))
        else:
            messages.error(
                request,
                'Furniture example could not be added,'
                'please check the form and try again.')
    else:
        form = FurnitureForm()

    template = 'furniture/add_furniture.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_furniture(request, furniture_id):
    """ Edit a furniture example in the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have'
                       'permission to perform this function.')
        return redirect(reverse('home'))

    furniture = get_object_or_404(Furniture, pk=furniture_id)
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES, instance=furniture)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('furniture_detail', args=[furniture.id]))
        else:
            messages.error(request,
                           'Failed to update item. '
                           'Please check form and try again.')
    else:
        form = FurnitureForm(instance=furniture)
        messages.info(request, f'You are editing {furniture.title}')

    template = 'furniture/edit_furniture.html'
    context = {
        'form': form,
        'furniture': furniture,
    }

    return render(request, template, context)


@login_required
def delete_furniture(request, furniture_id):
    """ Delete an item from the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have permission '
                       'to perform this function.')
        return redirect(reverse('home'))

    furniture = get_object_or_404(Furniture, pk=furniture_id)
    furniture.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('furniture'))
