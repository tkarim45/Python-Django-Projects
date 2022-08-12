from django import forms
from .models import post


class postform(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'author', 'content', 'Image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author', 'value': '', 'id': 'blogAuthor', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ente Content'}),
        }