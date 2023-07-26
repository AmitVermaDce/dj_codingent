from django.db import models
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

# Create your models here.

class Film(models.Model):
    name = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User, related_name="films")


    def get_absolute_url(self):
        return reverse("films:films-list")
