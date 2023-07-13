from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # Returns cleaned data of a specific field (i.e. title only) inside a dict
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the dummy":
    #         raise forms.ValidationError("Please enter some valid text for title")
    #     return title
    
    # Returns cleaned data of all the fields inside a dict
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the dummy":            
            self.add_error("title", "Please enter some valid text for title")
            if content == title:
                self.add_error("content", "Both title and content are same")
        return cleaned_data