'''
To render html pages
'''
from django.http import HttpResponse
from django.template.loader import render_to_string
import random
from articles.models import Article


def home_view(request):
    '''
    Take in request (Django sends request)
    Return HTML as a response (We pick to return the response)
    '''
    random_id = random.randint(1,3)
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "object": article_obj,
        "object_list": article_queryset,
        "id": random_id,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    HTML_STRING = render_to_string("home-view.html", context)       
    return HttpResponse(HTML_STRING)