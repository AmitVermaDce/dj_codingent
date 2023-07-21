from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):    
    error_css_class = ""
    required_css_class = 'required-field'
    name = forms.CharField(help_text="Help text for name field! <a href='/contact'>Contact Us</a>")
    # description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Recipe
        fields = ["name", "description", "directions"]

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
        