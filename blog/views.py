from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

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


@login_required
def add_blog(request):
    """Add blog article"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to perform this function.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Blog added!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(
                request, 'Blog could not be added, please check the form and try again.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit blog article """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to perform this function.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog. Please check form and try again.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete an item from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to perform this function.')
        return redirect(reverse('home'))
        
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blog'))