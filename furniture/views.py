from django.shortcuts import render
from .models import Furniture

# Create your views here.

def all_furniture(request):
    """View to return the art home page"""

    furniture = Furniture.objects.all()

    context = {
        'furniture': furniture,
    }
    
    return render(request, 'furniture/furniture.html', context)
