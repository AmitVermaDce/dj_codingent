from django.db import models
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)


    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)