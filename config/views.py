'''
To render html pages
'''
from django.http import HttpResponse
import random
from articles.models import Article


def home(request):
    '''
    Take in request (Django sends request)
    Return HTML as a response (We pick to return the response)
    '''
    random_id = random.randint(1,3)
    article_obj = Article.objects.get(id=random_id)
    H1_STRING = f"<h1>{article_obj.title}</h1>"
    P_STRING = f"<p>{article_obj.content}</p>" 
    F_STRING = f"<i>Object ID: {article_obj.id}</i>"
    return HttpResponse(H1_STRING +"\n" + P_STRING + "\n" + F_STRING)