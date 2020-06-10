from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')
    comments = Comment.objects.all().order_by('-id')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for word in post.content.split():
                if word.startswith('#'):
                    hashtag = HashTag.objects.get_or_create(name=word)[0] # (object, True or False)
                    post.tags.add(hashtag)
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
        liked = False
    else:
        post.like_users.add(user)
        liked = True

    context = {
        'liked': liked,
        'count': post.like_users.count(),
    }
    return JsonResponse(context)

@require_POST
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments_form = CommentForm(request.POST)
    if comments_form.is_valid():
        comment = comments_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()

    return JsonResponse({
        'id': comment.id,
        'postId': post_id,
        'username': comment.user.username,
        'comment': comment.comment,
    })

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

def hashtags(request, post_id):
    hashtag = get_object_or_404(HashTag, id=post_id)
    post = hashtag.taged_post.all()
    comments = Comment.objects.all().order_by('-id')
    comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'posts/index.html', context)

def search(request):
    target = request.GET.get('search')
    posts = Post.objects.filter(Q(content__contains=target))
    context = {
        'posts': posts,
        'target': target,
    }
    return render(request, 'posts/index.html', context)