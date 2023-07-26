from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Film
from django.views.generic.list import ListView

# Create your views here.
class FilmList(ListView):
    template_name = "films/films.html"
    model = Film
    context_object_name = 'films'

    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        return user.films.all()
    
def add_film_hx(request):
    film_name = request.POST.get("filmname")
    film = Film.objects.create(name=film_name)
    request.user.films.add(film)
    films = request.user.films.all()
    return render(request, "films/partials/films-list.html", {"films": films})

def delete_film_hx(request, pk):
    request.user.films.remove(pk)
    films = request.user.films.all()
    return render(request, "films/partials/films-list.html", {"films": films})