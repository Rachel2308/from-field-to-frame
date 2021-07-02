from django.shortcuts import render
from .models import Blog

# Create your views here.

def all_blogs(request):
    """View to return the blog home page"""

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }
    
    return render(request, 'blog/blogs.html', context)
