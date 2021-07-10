from django.shortcuts import render, get_object_or_404
from .models import Furniture

# Create your views here.

def all_furniture(request):
    """View to return the art home page"""

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