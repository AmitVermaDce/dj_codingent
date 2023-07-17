from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "slug", "content", "publish"]
    search_fields = ["content"]

admin.site.register(Article, ArticleAdmin)