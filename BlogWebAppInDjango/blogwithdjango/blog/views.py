from django.shortcuts import render
from .models import Post    # The dot before models means current directory or current application. 
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm

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


def post_detail(request, pk):
    """Get a single post or show 404 page

    Args:
        request everything received from user
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})