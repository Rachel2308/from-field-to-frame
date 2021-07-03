from django.shortcuts import render, get_object_or_404
from .models import Art

# Create your views here.

def all_art(request):
    """View to return the art home page"""

    art = Art.objects.all()

    context = {
        'art': art,
    }
    
    return render(request, 'art/art.html', context)

def art_detail(request, art_id):
    """View to return the art detail page"""

    art = get_object_or_404(Art, pk=art_id)

    context = {
        'art': art,
    }
    
    return render(request, 'art/art_detail.html', context)
