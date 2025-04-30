from django import forms
from tasks.models import Category


class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, label='Task Title')
    description = forms.CharField(widget=forms.Textarea, label='Task Description')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category')

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        if (title and description) and (title.lower() == description.lower()):
            raise forms.ValidationError("Title and description cannot be the same.")
        return cleaned_data
    

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
