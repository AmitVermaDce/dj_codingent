from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm
from django.http import HttpResponse, Http404
from django.urls import reverse

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
def recipe_delete_view(request, id=None):
    try:
        obj = Recipe.objects.get(id=id, user=request.user)        
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    
    if request.method == "POST":
        obj.delete()
        success_url = reverse('recipes:list')
        if request.htmx:
            headers = {
                "HX-Redirect": success_url,
            }
            return HttpResponse("Success", headers=headers)
        return redirect(success_url)
    context = {
        "object": obj
    }
    return render(request, "recipes/delete.html", context)


@login_required
def recipe_ingredient_delete_view(request, parent_id=None, id=None):
    try:
        obj = RecipeIngredient.objects.get(recipe__id=parent_id, id=id, recipe__user=request.user)        
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    
    if request.method == "POST":
        obj.delete()
        success_url = reverse('recipes:detail', kwargs={"id": parent_id,})
        if request.htmx:            
            # return HttpResponse("Ingredient Removed")
            return render(request, "recipes/partials/ingredient-inline-delete-response.html", {})
        return redirect(success_url)
    context = {
        "object": obj
    }
    return render(request, "recipes/delete.html", context)

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
        if request.htmx:
            headers = {
                "HX-Redirect": obj.get_absolute_url()
            }
            return HttpResponse("Created", headers=headers) 
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    recipe_form = RecipeForm(request.POST or None, instance=obj)  
    new_recipe_url = reverse("recipes:hx-ingredient-create", kwargs={"parent_id": obj.id})  
    context = {
        "recipe_form": recipe_form,
        "object": obj,
        "new_ingredient_url": new_recipe_url,
    }
    if recipe_form.is_valid():
        recipe_form.save()
        context["message"]='Data Saved.'   
    
    if request.htmx:
        return render(request, "recipes/partials/forms.html", context)
    return render(request, "recipes/create-update.html", context)


@login_required
def recipe_ingredient_update_hx_view(request, parent_id=None, id=None):
    # Doesn't take any other view other than htmx
    if not request.htmx:
        raise Http404
        
    # Only htmx views
    try:
        parent_obj = Recipe.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None
    if parent_obj is None:
        return HttpResponse("Not Found!!")
    instance = None
    if id is not None:
        try:
            instance = RecipeIngredient.objects.get(recipe=parent_obj, id=id)
        except:
            instance = None

    form = RecipeIngredientForm(request.POST or None, instance=instance)
    url = reverse("recipes:hx-ingredient-create", kwargs={"parent_id": parent_obj.id})
    if instance:
        url = instance.get_hx_edit_url()
    context = {
        "url": url,
        "object": instance,
        "form": form
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context["object"] = new_obj
        return render(request, "recipes/partials/ingredient-inline.html", context)    
    return render(request, "recipes/partials/ingredient-form.html", context)
    

        
