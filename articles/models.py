from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    print("Artilcle Pre_save method is called")
    if instance.slug is None:
        instance = slugify_instance_title(instance)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    print("Article Post_save method is called")
    if created:
        instance = slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)