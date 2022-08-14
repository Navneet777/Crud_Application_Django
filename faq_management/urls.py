from django.urls import path
from .views import *
urlpatterns = [
    path('', FAQView.as_view(), name="faq_list"),
    path("<int:pk>", FAQDetailedView.as_view(), name="faq_detail_view"),
    path('add_faq', AddFAQView.as_view(), name="add_faq"),
    path('edit_faq/<int:pk>', EditFAQView.as_view(), name="edit_faq"),
    path('delete_faq/<int:pk>', DeleteFAQView.as_view(), name="delete_faq")
    ]
