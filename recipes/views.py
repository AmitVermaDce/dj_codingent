from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm
from django.http import HttpResponse

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
def recipe_detail_hx_view(request, id=None):
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        return HttpResponse("Not Found!!")
    context = {
        "object": obj
    }
    return render(request, "recipes/partials/detail.html", context)
    


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
    RecipeIngredientFormset = modelformset_factory(RecipeIngredient, 
                                            form=RecipeIngredientForm,
                                            extra=0)
    qs = obj.recipeingredient_set.all()
    formset = RecipeIngredientFormset(request.POST or None, queryset=qs)   
    context = {
        "recipe_form": recipe_form,
        "formset": formset,
        "object": obj,
    }
    
    if all([recipe_form.is_valid(), formset.is_valid()]):
        parent = recipe_form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            child.recipe = parent                
            child.save()
        context["message"] = "Data saved."
        # return redirect(obj.get_absolute_url())
    
    if request.htmx:
        return render(request, "recipes/partials/forms.html", context)
    return render(request, "recipes/create-update.html", context)