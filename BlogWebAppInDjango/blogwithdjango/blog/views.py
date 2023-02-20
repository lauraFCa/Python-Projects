from django.shortcuts import render
from .models import Post    # The dot before models means current directory or current application. 
from django.utils import timezone


def homepage(request):
    """Render the home page

    Args:
        request: everything received from user

    Returns:
        The reendered page: Home page
    """
    return render(request, 'blog/index.html', {})


def post_list(request):
    """Render Posts list view

    Args:
        request: everything received from user

    Returns:
        The reendered page: List of posts in published date order
    """
    # order posts using Queryset
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

