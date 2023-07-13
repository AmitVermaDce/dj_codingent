from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


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
    form = ArticleForm()
     # print(dir(form)) # To view all methods linked with the form object
    context = {
        "form": form
    }
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        context["form"] = form
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            context["object"] = Article.objects.create(title=title, content=content)
            context["created"] = True   
    return render(request, 'articles/create.html', context)

