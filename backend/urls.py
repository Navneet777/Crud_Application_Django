from django.contrib import admin
from django.urls import path,include
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('category_management.urls')),
    path('news_management/', include('news_management.urls')),
    path('blog_management/', include('blog_management.urls')),
    path('faq_management/', include('faq_management.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
