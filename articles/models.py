from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)