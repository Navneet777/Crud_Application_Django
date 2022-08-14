from django.urls import path
from .views import *

urlpatterns = [
    # path('add', views.add, name="add"),
    path('', CategoryView.as_view(), name="category_list"),
    path("<int:pk>", CategoryDetailedView.as_view(), name="category_detail_view"),
    path('category_management/add_category', AddCategoryView.as_view(), name="add_category"),
    path('category_management/edit_category/<int:pk>', EditCategoryView.as_view(), name="edit_category"),
    path('category_management/delete_category/<int:pk>', DeleteCategoryView.as_view(), name="delete_category")
    ]
