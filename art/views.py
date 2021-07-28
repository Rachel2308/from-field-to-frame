from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Art
from .forms import ArtForm

# Create your views here.

def all_art(request):
    """View to return the art home page"""

    art = Art.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        art = art.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'art': art,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'art/art.html', context)

def art_detail(request, art_id):
    """View to return the art detail page"""

    art = get_object_or_404(Art, pk=art_id)

    context = {
        'art': art,
    }
    
    return render(request, 'art/art_detail.html', context)


@login_required
def add_art(request):
    """Add art to store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to perform this function.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save()
            messages.success(request, 'Item added!')
            return redirect(reverse('art_detail', args=[art.id]))
        else:
            messages.error(
                request, 'Product could not be added, please check the form and try again.')
    else:
        form = ArtForm()

    template = 'art/add_art.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_art(request, art_id):
    """ Edit a item of art in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to perform this function.')
        return redirect(reverse('home'))

    art = get_object_or_404(Art, pk=art_id)
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES, instance=art)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('art_detail', args=[art.id]))
        else:
            messages.error(request, 'Failed to update item. Please check form and try again.')
    else:
        form = ArtForm(instance=art)
        messages.info(request, f'You are editing {art.title}')

    template = 'art/edit_art.html'
    context = {
        'form': form,
        'art': art,
    }

    return render(request, template, context)


@login_required
def delete_art(request, art_id):
    """ Delete an item from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to perform this function.')
        return redirect(reverse('home'))
        
    art = get_object_or_404(Art, pk=art_id)
    art.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('art'))