from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):    
    error_css_class = ""
    required_css_class = 'require-field'
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Recipe Name"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 3
    }))

    class Meta:
        model = Recipe
        fields = ["name", "description", "directions",]


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["name", "quantity", "unit"]
        