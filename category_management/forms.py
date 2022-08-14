from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    options = (
        ('NEWS', 'News'),
        ('ARTICAL', 'Artical'),
        ('BLOG', 'Blog'),
        ('FAQ', 'Faq'),
        ('LEGAL TERMS', 'Legal Terms'),
    )
    published_options = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control'}))
    published = forms.CharField(widget=forms.Select(choices=published_options, attrs={'class': 'form-control'}))
    class Meta:
        model = Category
        fields = ['name', 'type', 'published']