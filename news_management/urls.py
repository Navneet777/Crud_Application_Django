from django.urls import path
from . import views
urlpatterns = [
    path('add_news', views.add_news,name="addnews"),
]
