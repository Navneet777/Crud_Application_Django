from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryView.as_view(), name="category_list"),
    path("<int:pk>", CategoryDetailedView.as_view(), name="category_detail_view"),
    path('add_category', AddCategoryView.as_view(), name="add_category"),
    path('edit_category/<int:pk>', EditCategoryView.as_view(), name="edit_category"),
    path('delete_category/<int:pk>', DeleteCategoryView.as_view(), name="delete_category")
    ]
