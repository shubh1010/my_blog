from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Post, Topic, Comment, PhotoContestSubmission

# Inline for comments in the Post admin
class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('name', 'email', 'text', 'approved')
    readonly_fields = ('name', 'email', 'text')
    extra = 0  # Don't show extra empty forms

# Admin for posts
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    ordering = ('-created',)
    search_fields = ('title', 'author__username', 'author__first_name', 'author__last_name')
    list_filter = ('status', 'topics')
    inlines = [CommentInline]

# Admin for topics
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

# Admin for comments
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'approved', 'created')
    list_filter = ('approved', 'created')
    search_fields = ('name', 'email', 'text')

# Admin for photo contest submissions
class PhotoContestSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submission_date', 'image_preview')
    list_filter = ('submission_date',)
    search_fields = ('name', 'email')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = 'Photo Preview'

# Register models with the default admin site (unchanged)
admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PhotoContestSubmission, PhotoContestSubmissionAdmin)

# Add "View Site" link in the admin header (top-left)
admin.site.site_header = format_html(
    'My Blog Admin - <a href="{}" target="_blank" style="color:white; text-decoration: underline;">View Site</a>',
    reverse('home')
)

# --- Restrict access to superusers only, by patching the permission check of the default admin site ---

def superusers_only_has_permission(self, request):
    """
    Allow access only to active superusers (no staff-only access).
    """
    return request.user.is_active and request.user.is_superuser

admin.site.has_permission = superusers_only_has_permission.__get__(admin.site)
