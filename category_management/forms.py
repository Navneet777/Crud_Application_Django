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
    TRUE_FALSE_CHOICES = ((True, 'Yes'),(False, 'No'))
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control'}))
    # published = forms.CharField(widget=forms.Select(choices=published_options, attrs={'class': 'form-control'}))
    # published = forms.BooleanField(required=False)
    published = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="published", initial='', widget=forms.CheckboxInput(), required=True)
    class Meta:
        model = Category
        fields = ['name', 'type', 'published']