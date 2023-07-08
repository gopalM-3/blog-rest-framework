from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    class BlogObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='published')

    options = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    hashtags = models.TextField(null=True)
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()
    blogobjects = BlogObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self) -> str:
        return self.title
