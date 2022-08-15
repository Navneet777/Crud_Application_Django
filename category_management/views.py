from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category
from .forms import CategoryForm
class CategoryView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'category_management/list_view.html'
    context_object_name = 'category_list'

class CategoryDetailedView(DetailView):
    model = Category
    template_name = 'category_management/detail_view.html'
    context_object_name = 'category_detail'

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_management/add_category.html'
    success_url = '/'

class EditCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    pk_url_kwarg = 'pk'
    template_name = 'category_management/edit_category.html'
    success_url = '/'

class DeleteCategoryView(DeleteView):
    model = Category
    pk_url_kwarg = 'pk'
    template_name = 'category_management/delete_view.html'
    success_url = '/'
