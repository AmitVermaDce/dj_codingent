from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


# Create your views here.
def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except:
            raise Http404

    context = {
        "object": article_obj,
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    
    return render(request, "articles/detail.html", context)


def article_search_view(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get('query'))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }

    return render(request, "articles/search.html", context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_obj = form.save()
        context["form"] = ArticleForm()
        context["object"] = article_obj
        context["created"] = True 
    return render(request, 'articles/create.html', context)

