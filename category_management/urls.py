from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryView.as_view(), name="category_list"),
    path("<int:pk>", CategoryDetailedView.as_view(), name="category_detail_view"),
    path('add_category', AddCategoryView.as_view(), name="add_category"),
    path('edit_category/<int:pk>', EditCategoryView.as_view(), name="edit_category"),
    path('delete_category/<int:pk>', DeleteCategoryView.as_view(), name="delete_category"),
    path('', BlogView.as_view(), name="blog_list"),
    path("<int:pk>", BlogDetailedView.as_view(), name="blog_detail_view"),
    path('add_blog', AddBlogView.as_view(), name="add_blog"),
    path('edit_blog/<int:pk>', EditBlogView.as_view(), name="edit_blog"),
    path('delete_blog/<int:pk>', DeleteBlogView.as_view(), name="delete_blog"),
    path('', FAQView.as_view(), name="faq_list"),
    path("<int:pk>", FAQDetailedView.as_view(), name="faq_detail_view"),
    path('add_faq', AddFAQView.as_view(), name="add_faq"),
    path('edit_faq/<int:pk>', EditFAQView.as_view(), name="edit_faq"),
    path('delete_faq/<int:pk>', DeleteFAQView.as_view(), name="delete_faq"),
    path('', NewsView.as_view(), name="news_list"),
    path("<int:pk>", NewsDetailedView.as_view(), name="news_detail_view"),
    path('add_news', AddNewsView.as_view(), name="add_news"),
    path('edit_news/<int:pk>',EditNewsView.as_view(), name="edit_news"),
    path('delete_news/<int:pk>', DeleteNewsView.as_view(), name="delete_news")
    ]
