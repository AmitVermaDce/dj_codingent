from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RecipeIngredientForm

# CRUD: Create Retrieve Update & Delete

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        "object_list": qs,
    }
    return render(request, "recipes/search.html", context)


@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        "object": obj,
    }
    return render(request, "recipes/detail.html", context)


@login_required
def recipe_create_view(request, id=None):
    form = RecipeForm(request.POST or None)  
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()  
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form_recipe = RecipeForm(request.POST or None, instance=obj)   
    form_ingredient = RecipeIngredientForm(request.POST or None)
    context = {
        "form_recipe": form_recipe,
        "form_ingredient": form_ingredient,
        "object": obj,
    }
    if all([form_recipe.is_valid(), form_ingredient.is_valid()]):
        parent = form_recipe.save(commit=False)
        parent.save()
        child = form_ingredient.save(commit=False)
        child.recipe = parent
        child.save()
        print("form_recipe", form_recipe.cleaned_data)
        print("form_ingredient", form_ingredient.cleaned_data)
        context["message"] = "Data saved."
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)