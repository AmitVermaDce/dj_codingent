from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains = query) | Q(content__icontains = query)        
        return self.filter(lookups)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
      

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=220)
    content = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)

    objects = ArticleManager()

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={"slug": self.slug})
        # return f"/articles/{self.slug}/"
    
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