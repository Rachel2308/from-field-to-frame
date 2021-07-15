from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    """View to return the blog home page"""

    blog = Blog.objects.all()
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
        blog = blog.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'blog': blog,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'blog/blogs.html', context)


def blog_detail(request, blog_id):
    """View to return the blog detail page"""

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }
    
    return render(request, 'blog/blog_detail.html', context)
