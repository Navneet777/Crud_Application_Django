from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Blog
from .forms import BlogForm
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
    success_url = '/blog_management'

class EditBlogView(UpdateView):
    model = Blog
    form_class = BlogForm
    pk_url_kwarg = 'pk'
    template_name = 'blog_management/edit_blog.html'
    success_url = '/blog_management'

class DeleteBlogView(DeleteView):
    model = Blog
    pk_url_kwarg = 'pk'
    template_name = 'blog_management/delete_view.html'
    success_url = '/blog_management'
