from django.urls import path
from .views import (
    FilmList,
    add_film_hx,
)

app_name = "films"
urlpatterns = [
    path("films-list/", FilmList.as_view(), name="films-list"),
    
]

# HTMX url patterns
htmx_urlpatterns = [
    path("add-films/", add_film_hx, name="add-films"),
]

urlpatterns += htmx_urlpatterns