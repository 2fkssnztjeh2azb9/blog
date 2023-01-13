from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def index(request):
    posts = BlogPost.objects.order_by('-date_added')    
    context = {"posts": posts}
    return render(request, 'blogs/index.html', context)

def check_user(request, post):
    if post.owner != request.user:
        raise Http404
    
@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    check_user(request, post)

    if request.method != "POST":
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('blogs:index')

    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def new_post(request):
    if not request.user.id:
        raise Http404
    if request.method != "POST":
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def my_posts(request):
    posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')    
    context = {"posts": posts}
    return render(request, 'blogs/my_posts.html', context)

def post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {"post": post}
    return render(request, 'blogs/post.html', context)
