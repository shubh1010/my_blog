from django.contrib.auth.models import User
from blog.models import Post, Topic, Comment
from django.db.models import Count, Q

def question_1_return_active_users():
    return Post.objects.values_list('author__username').annotate(post_count=Count('id'))

def question_2_return_all_draft_posts():
    return Post.objects.filter(status='draft')

def question_3_return_all_published_posts_ordered_by_date():
    return Post.objects.filter(status='published').order_by('-published')

def question_4_return_posts_containing_python():
    return Post.objects.filter(Q(title__icontains='python') | Q(content__icontains='python'))

def question_5_return_all_posts_by_author(author_name):
    return Post.objects.filter(author__username=author_name)

def question_6_return_all_comments_on_post(post_id):
    return Comment.objects.filter(post__id=post_id)

def question_7_return_all_posts_with_multiple_topics():
    return Post.objects.annotate(topic_count=Count('topics')).filter(topic_count__gt=1)

def question_8_return_all_topics_alphabetically():
    return Topic.objects.order_by('name')

def question_9_return_number_of_comments_for_each_post():
    return Post.objects.annotate(num_comments=Count('comments')).values_list('title', 'num_comments')