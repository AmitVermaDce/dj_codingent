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
    content = {
        "id": random_id,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    HTML_STRING = '''
    <i>Object ID: {id}</i>
    <h1>{title}</h1>
    <p>{content}</p>
    '''.format(**content)    
    return HttpResponse(HTML_STRING)