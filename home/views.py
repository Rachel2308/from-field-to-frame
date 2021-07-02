from django.shortcuts import render

# Create your views here.

def index(request):
    """View to return the index page"""
    
    return render(request, 'home/index.html')


def contact(request):
    """View to return the contact page"""
    
    return render(request, 'home/contact.html')