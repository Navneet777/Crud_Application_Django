from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name="news_list"),
    path("<int:pk>", NewsDetailedView.as_view(), name="news_detail_view"),
    path('add_news', AddNewsView.as_view(), name="add_news"),
    path('edit_news/<int:pk>',EditNewsView.as_view(), name="edit_news"),
    path('delete_news/<int:pk>', DeleteNewsView.as_view(), name="delete_news")
    ]
