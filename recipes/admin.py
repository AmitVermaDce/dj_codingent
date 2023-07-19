from django.contrib import admin
from .models import RecipeIngredient, Recipe

admin.site.register(RecipeIngredient)

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0    
    readonly_fields = ["quantity_as_float", "as_mks", "as_imperial", "to_ounces"]
    # fields = ["name", "quantity", "unit", "directions", "quantity_as_float"]


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, ]
    list_display = ["name", "user"]
    readonly_fields = ["timestamp", "updated"]
    raw_id_fields = ["user"]
 

admin.site.register(Recipe, RecipeAdmin)