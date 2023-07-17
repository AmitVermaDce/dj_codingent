from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q
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
    query = request.GET.get("query")
    qs = Article.objects.all()
    if query is not None:
        lookups = Q(title__icontains = query) | Q(content__icontains = query)
        qs = Article.objects.filter(lookups)
    print(qs)
    context = {
        "objects": qs,
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
        # return redirect("article-detail", slug=article_obj.slug)
        return redirect(article_obj.get_absolute_url())
    return render(request, 'articles/create.html', context)

