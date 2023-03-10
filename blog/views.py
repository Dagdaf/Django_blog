from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import *
from blog.forms import *


def post_list(request):
    posts = Post.objects.filter(published=True)
    category = Categories.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})


def post_draft(request):
    posts = Post.objects.filter(published=False)
    return render(request, 'blog/post_list.html', {'posts': posts})


def published_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.published = True
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})


def rating(post_pk):
    comments = Comments.objects.filter(post=post_pk)
    if comments.count() == 0:
        count = 0
    else:
        count = sum([i.rating for i in comments]) / comments.count()
    return round(count, 1)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = Comments.objects.filter(post=post_pk)
    counter = Comments.objects.filter(post=post_pk).count()
    post_rating = post.rating
    if request.method == "GET":
        form = CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'counter': counter, 'form': form, 'post_rating': post_rating})
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.publish_date = datetime.now()
            comment.save()
            post.rating = rating(post_pk)
            post.save()
            return redirect('post_detail', post_pk=post.pk)



def post_new(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    form = PostForm()


def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect('post_list')


def comment_delete(request, comment_pk, post_pk):
    post = Post.objects.get(pk=post_pk)
    counter = Comments.objects.filter(post=post_pk).count()
    comment = get_object_or_404(Comments, pk=comment_pk).delete()
    post.rating = rating(post_pk)
    post.save()
    return redirect('post_detail', post_pk=post.pk)


def category_posts(request, category_pk):
    category = Categories.objects.all()
    posts = Post.objects.filter(category=category_pk)
    context = {'category': category, 'posts': posts}
    return render(request, 'blog/post_list.html', context)


def recommends(request):
    posts = Post.objects.filter(published=True).order_by('-rating')
    return render(request, 'blog/post_list.html', {'posts': posts})



