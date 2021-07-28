from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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

def add_art(request):
    """Add art to store"""
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added!')
            return redirect(reverse('art'))
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