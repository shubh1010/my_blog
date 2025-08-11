from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import the custom logout view you created
from blog.views import CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main app URLs
    path('', include('blog.urls')),

    # CKEditor upload URL routes
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Override logout path to use CustomLogoutView instead of default
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),

    # Include all other auth URLs except logout (login, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve media files during development (Pillow image uploads, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
