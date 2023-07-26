from django.urls import path
from .views import (
    FilmList,
    add_film_hx,
    delete_film_hx,
)

app_name = "films"
urlpatterns = [
    path("films-list/", FilmList.as_view(), name="films-list"),
    
]

# HTMX url patterns
htmx_urlpatterns = [
    path("add-film/", add_film_hx, name="add-film"),
    path("delete-film/<int:pk>/", delete_film_hx, name="delete-film"),
]

urlpatterns += htmx_urlpatterns