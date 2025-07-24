from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Topic

class TopicListView(ListView):
    model = Topic
    template_name = 'blog/topic_list.html'
    context_object_name = 'topics'
    ordering = ['name']  # Alphabetical order

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'blog/topic_detail.html'
    context_object_name = 'topic'

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})