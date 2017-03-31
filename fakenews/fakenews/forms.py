from django import forms

class SearchForm(forms.ModelForm):
    search_query = forms.CharField(max_length=100)