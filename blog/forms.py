from django import forms
from .models import Post, Category

category_choices = Category.objects.all().values_list('name', 'name')

category_choices_list = []

for item in category_choices:
    category_choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'article_snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class ': 'form-control', 'value': '', 'id': 'author', 'type': 'hidden'}),
            'category': forms.Select(choices=category_choices_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'article_snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
