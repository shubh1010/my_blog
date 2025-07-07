from django.contrib import admin
from django.urls import path, include
from blog import views  # Make sure blog is in INSTALLED_APPS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='home'),  # Root URL shows published blog posts
    path('posts/', include('blog.urls')),    # Routes for detailed post views etc.
]