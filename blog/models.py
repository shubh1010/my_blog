from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# ✅ Import CKEditor rich text upload field
from ckeditor_uploader.fields import RichTextUploadingField


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)

    # ✅ Changed from TextField to RichTextUploadingField
    content = RichTextUploadingField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    topics = models.ManyToManyField(Topic, blank=True)

    class Meta:
        ordering = ['-published']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status == 'published' and not self.published:
            self.published = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=1000)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


# New model for the photo contest
class PhotoContestSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='contest_images/')
    submission_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submission_date']

    def __str__(self):
        return f"{self.name} - {self.submission_date.strftime('%Y-%m-%d %H:%M')}"
