from django.contrib import admin
from .models import Post, Topic, Comment

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

# Register everything
admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)