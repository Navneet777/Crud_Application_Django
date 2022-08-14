from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    status_choice = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    )
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    short_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField()
    status = forms.CharField(widget=forms.Select(choices=status_choice, attrs={'class': 'form-control'}))
    meta_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    meta_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    meta_keyword = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    og_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    og_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    og_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    canonical_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = FAQ
        fields = ['title', 'short_description', 'description','image','status','meta_title','meta_description','meta_keyword','og_title','og_description','og_url','canonical_url']