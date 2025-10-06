from django import forms
from .models import Post, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'text', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'text': forms.Textarea(attrs={'rows': 8}),
        }
