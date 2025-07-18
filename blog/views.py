from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from .models import Post, Topic


def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-created')

    # Annotate each topic with the number of published posts
    topics = Topic.objects.annotate(
        post_count=Count('post', filter=Q(post__status='published'))
    ).order_by('-post_count')[:10]

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'topics': topics,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})