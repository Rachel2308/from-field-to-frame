from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    """View to return the blog home page"""

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }
    
    return render(request, 'blog/blogs.html', context)


def blog_detail(request, blog_id):
    """View to return the blog detail page"""

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }
    
    return render(request, 'blog/blog_detail.html', context)
