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
    recipe_form = RecipeForm(request.POST or None)  
    context = {
        "recipe_form": recipe_form
    }
    if recipe_form.is_valid():
        obj = recipe_form.save(commit=False)
        obj.user = request.user
        obj.save()  
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    recipe_form = RecipeForm(request.POST or None, instance=obj)   
    ingredient_forms = []
    for ingredient_obj in obj.recipeingredient_set.all():
        ingredient_forms.append(
            RecipeIngredientForm(request.POST or None, instance=ingredient_obj)
        )

    context = {
        "recipe_form": recipe_form,
        "ingredient_forms": ingredient_forms,
        "object": obj,
    }
    all_ingredient_forms = all([form.is_valid() for form in ingredient_forms])
    if all_ingredient_forms and recipe_form.is_valid():
        parent = recipe_form.save(commit=False)
        parent.save()
        for each_ingredient_form in ingredient_forms:
            child = each_ingredient_form.save(commit=False)
            child.recipe = parent
            child.save()
        context["message"] = "Data saved."
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)