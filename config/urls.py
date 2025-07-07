from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='home'),  # Homepage shows published blog posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Individual post page
]