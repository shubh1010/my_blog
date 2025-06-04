from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),      # Root URL serves the index view (welcome message)
    path('home/', views.home, name='home'),   # /home/ URL serves the blog posts listing
]
