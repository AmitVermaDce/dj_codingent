from django.urls import path

from .views import (
    recipe_list_view,
    recipe_detail_view,
    recipe_detail_hx_view,
    recipe_create_view,
    recipe_update_view,
)

app_name = "recipes"
urlpatterns = [
    path("", recipe_list_view, name="search"),
    path("create/", recipe_create_view, name="create"),
    path("<int:id>/", recipe_detail_view, name="detail"),
    path("hx/<int:id>/", recipe_detail_hx_view, name="hx-detail"),
    path("<int:id>/edit/", recipe_update_view, name="update"),
]