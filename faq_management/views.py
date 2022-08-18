from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import FAQ
from .forms import FAQForm
from django.urls import reverse_lazy
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
