from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Title Tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something amazing!'}),
        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Title Tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something amazing!'}),
        }