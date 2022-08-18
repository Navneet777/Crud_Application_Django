from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import News
from .forms import NewsForm
from django.urls import reverse_lazy
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
