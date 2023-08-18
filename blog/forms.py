"""Forms for creating comments and recipes on the website"""
from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """Comment input form"""
    class Meta:
        "Metadata about form"
        model = Comment
        fields = ('content',)
        labels = {
            'content': ''
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Comment',
                'rows': '4',
                'cols': '40'}),
        }


class RecipeForm(forms.ModelForm):
    """User Recipe Entry Form"""
    class Meta:
        """User Recipe Entry Form"""
        model = Recipe
        fields = (
            'title',
            'status',
            'image',
            'image_alt',
            'season',
            'summary',
            'ingredients',
            'instructions',
            'tags'
        )
        labels = {
            'image_alt': 'Image Description'
            }
        widgets = {}
