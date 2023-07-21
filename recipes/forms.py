from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):    
    error_css_class = ""
    required_css_class = 'require-field'
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "form-control",
    #     "placeholder": "Recipe Name"
    # }))
    # description = forms.CharField(widget=forms.Textarea(attrs={
    #     "class": "form-control",
    #     "rows": 3
    # }))

    class Meta:
        model = Recipe
        fields = ["name", "description", "directions",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {"class": "form-control-2",
                 "placeholder": f"Recipe {field}"})
            self.fields["description"].widget.attrs.update({"row": "3"})
            self.fields["directions"].widget.attrs.update({"row": "5"})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["name", "quantity", "unit"]
        