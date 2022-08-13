from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category_management/', include('category_management.urls')),
    path('news_management/', include('news_management.urls')),
    path('blog_management/', include('blog_management.urls')),
    path('faq_management/', include('faq_management.urls')),
]
