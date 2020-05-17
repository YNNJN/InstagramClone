from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.add_message(request, messages.INFO, 'Your post has been successfully submitted!')
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Your post has been successfully deleted!')
    return redirect('posts:index')

@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post_ = form.save(commit=False)
                post_.user = request.user
                post_.save()
                messages.add_message(request, messages.SUCCESS, 'Your post has been successfully updated!')
                return redirect('posts:index')
        else:
            form = PostForm(instance=post)
        context = {
            'form': form,
            'post': post,
        }
        return render(request, 'posts/form.html', context)
    else:
        messages.add_message(request, messages.INFO, 'You are not authorized.')
        return redirect('posts:index')

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:index')

@require_POST
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments_form = CommentForm(request.POST)
    if comments_form.is_valid():
        comment = comments_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect('posts:detail', post_id)

@login_required
def comment_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comments_form = CommentForm()
    if comment.user == request.user:
        comment.delete()
        context = {
            'post': post,
            'comment_form': comment_form,
        }
        messages.add_message(request, messages.INFO, 'Comment deleted')
        return render(request, 'posts/detail.html', context)
    else:
        messages.danger(request, 'You are not authorized.')
        return redirect('accounts:login')
