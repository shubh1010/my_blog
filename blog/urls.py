from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('topics/', views.TopicListView.as_view(), name='topic_list'),
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]