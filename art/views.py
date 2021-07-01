from django.shortcuts import render
from .models import Art

# Create your views here.

def all_art(request):
    """View to return the art home page"""

    art = Art.objects.all()

    context = {
        'art': art,
    }
    
    return render(request, 'art/art.html', context)

