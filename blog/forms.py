from django import forms
from .models import Post, Category, Profile, Comment

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
            'article_snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }