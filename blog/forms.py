from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': ''
        }
        widgets = {
            'content': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Comment'})
        }
