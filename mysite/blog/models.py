import hashlib
from django.utils.text import slugify
from django.db import models


class Post(models.Model):
    content = models.TextField()
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    img = models.ImageField(upload_to="static/img", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ("anonymous", "Anonymous"),
        ("published", "Published"),
    ]
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="published"
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)[:50]
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = (
                    slugify(self.content)[:50]
                    + "-"
                    + hashlib.sha1(self.content.encode("utf-8")).hexdigest()[:8]
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
