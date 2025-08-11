from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('topics/', views.TopicListView.as_view(), name='topic_list'),
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('photo-contest/', views.photo_contest_submission, name='photo_contest_submission'),
    path('photo-contest/submissions/', views.photo_contest_submissions_list, name='photo_contest_submissions_list'),
    path('signup/', views.signup, name='signup'),

    # ✅ Custom logout view to avoid blank page and redirect home
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'),

    # ✅ Let Django handle login and other auth views automatically
    path('accounts/', include('django.contrib.auth.urls')),

    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
