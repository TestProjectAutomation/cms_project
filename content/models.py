from django.db import models
from django.conf import settings

# Create your models here.
class Content(models.Model):
    CONTENT_TYPE = (
        ('page', 'Page'),
        ('post', 'Post'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE)
    status = models.CharField(
        max_length=10,
        choices=(('draft', 'Draft'), ('published', 'Published'))
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
