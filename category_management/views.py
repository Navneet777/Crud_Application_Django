from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Blog, FAQ , News
from .forms import CategoryForm, BlogForm , FAQForm , NewsForm
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('category_list')

class EditCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    pk_url_kwarg = 'pk'
    template_name = 'category_management/edit_category.html'
    success_url = reverse_lazy('category_list')

class DeleteCategoryView(DeleteView):
    model = Category
    pk_url_kwarg = 'pk'
    template_name = 'category_management/delete_view.html'
    success_url = reverse_lazy('category_list')

class BlogView(ListView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog_management/list_view.html'
    context_object_name = 'blog_list'

class BlogDetailedView(DetailView):
    model = Blog
    template_name = 'blog_management/detail_view.html'
    context_object_name = 'blog_detail'

class AddBlogView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_management/add_blog.html'
    success_url = reverse_lazy('blog_list')

class EditBlogView(UpdateView):
    model = Blog
    form_class = BlogForm
    pk_url_kwarg = 'pk'
    template_name = 'blog_management/edit_blog.html'
    success_url = reverse_lazy('blog_list')
class DeleteBlogView(DeleteView):
    model = Blog
    pk_url_kwarg = 'pk'
    template_name = 'blog_management/delete_view.html'
    success_url = reverse_lazy('blog_list')

class FAQView(ListView):
    model = FAQ
    queryset = FAQ.objects.all()
    template_name = 'faq_management/list_view.html'
    context_object_name = 'faq_list'

class FAQDetailedView(DetailView):
    model = FAQ
    template_name = 'faq_management/detail_view.html'
    context_object_name = 'faq_detail'

class AddFAQView(CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'faq_management/add_faq.html'
    success_url = reverse_lazy('faq_list')

class EditFAQView(UpdateView):
    model = FAQ
    form_class = FAQForm
    pk_url_kwarg = 'pk'
    template_name = 'faq_management/edit_faq.html'
    success_url = reverse_lazy('faq_list')

class DeleteFAQView(DeleteView):
    model = FAQ
    pk_url_kwarg = 'pk'
    template_name = 'faq_management/delete_view.html'
    success_url = reverse_lazy('faq_list')

class NewsView(ListView):
    model = News
    queryset = News.objects.all()
    template_name = 'news_management/list_view.html'
    context_object_name = 'news_list'

class NewsDetailedView(DetailView):
    model = News
    template_name = 'news_management/detail_view.html'
    context_object_name = 'news_detail'

class AddNewsView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news_management/add_news.html'
    success_url = reverse_lazy('news_list')

class EditNewsView(UpdateView):
    model = News
    form_class = NewsForm
    pk_url_kwarg = 'pk'
    template_name = 'news_management/edit_news.html'
    success_url = reverse_lazy('news_list')

class DeleteNewsView(DeleteView):
    model = News
    pk_url_kwarg = 'pk'
    template_name = 'news_management/delete_view.html'
    success_url = reverse_lazy('news_list')