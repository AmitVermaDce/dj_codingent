'''
To render html pages
'''
from django.http import HttpResponse
import random




def home(request):
    '''
    Take in request (Django sends request)
    Return HTML as a response (We pick to return the response)
    '''
    name = "John F Kennedy"
    number = random.randint(1, 2344447)
    H1_STRING = f'''
    <h1>Hello "{name}" - {number}</h1>
    '''
    P_STRING = '''
    <p>Dummy Text: 
    <small>Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
    It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
    sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
    like Aldus PageMaker including versions of Lorem Ipsum.</small></p>
    ''' 
    return HttpResponse(H1_STRING +"\n" + P_STRING)