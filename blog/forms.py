from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    "Comment input form"
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
