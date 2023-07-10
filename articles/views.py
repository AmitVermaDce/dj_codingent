from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail_view(request, id=None):
    article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
        "id": id,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    
    return render(request, "articles/detail.html", context)
