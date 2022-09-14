from django import forms
from .models import Category,Blog, FAQ,News


class CategoryForm(forms.ModelForm):
    options = (
        ('NEWS', 'News'),
        ('ARTICAL', 'Artical'),
        ('BLOG', 'Blog'),
        ('FAQ', 'Faq'),
        ('LEGAL TERMS', 'Legal Terms'),
    )
    TRUE_FALSE_CHOICES = ((True, 'Yes'),(False, 'No'))
    type = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control'}))
    published = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="published", initial='', widget=forms.CheckboxInput(), required=True)
    class Meta:
        model = Category
        fields = ['name', 'type', 'published']

class BlogForm(forms.ModelForm):
    model = Blog
    fields = ['title', 'short_description', 'description','image','status','meta_title','meta_description','meta_keyword','og_title','og_description','og_url','canonical_url']

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['title', 'short_description', 'description','image','status','meta_title','meta_description','meta_keyword','og_title','og_description','og_url','canonical_url']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'short_description', 'description','image','status','meta_title','meta_description','meta_keyword','og_title','og_description','og_url','canonical_url']