from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout  # ✅ Explicit logout function
from .models import Post, Topic, PhotoContestSubmission
from . import forms
from django.contrib.admin.views.decorators import staff_member_required


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


def form_example(request):
    form = forms.ExampleSignupForm()
    return render(request, 'blog/form_example.html', context={'form': form})


def photo_contest_submission(request):
    if request.method == 'POST':
        form = forms.PhotoContestSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'blog/photo_contest_success.html')
    else:
        form = forms.PhotoContestSubmissionForm()
    return render(request, 'blog/photo_contest_submission.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect('login')
    else:
        form = forms.SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@staff_member_required
def photo_contest_submissions_list(request):
    submissions = PhotoContestSubmission.objects.all().order_by('-submission_date')
    return render(request, 'blog/photo_contest_submissions_list.html', {
        'submissions': submissions
    })


# ✅ Fixed: Explicitly logs the user out before redirecting
class CustomLogoutView(LogoutView):
    """
    Logs the user out and redirects to home.
    Works regardless of GET/POST request method.
    """
    def dispatch(self, request, *args, **kwargs):
        logout(request)  # ✅ Clear the session
        return redirect('/')  # ✅ Go to home page after logout