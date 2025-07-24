from django.db.models import Count, Q
from .models import Topic

def top_topics(request):
    topics = Topic.objects.annotate(
        post_count=Count('post', filter=Q(post__status='published'))
    ).order_by('-post_count')[:10]
    return {'topics': topics}