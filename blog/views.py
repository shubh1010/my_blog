from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    return HttpResponse("Welcome to My Blog")

def home(request):
    posts = Post.objects.all().order_by('-id')  # newest first
    return render(request, 'blog/home.html', {'posts': posts})