from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('category_management/', include('category_management.urls')),
    path('news_management/', include('news_management.urls')),
    path('blog_management/', include('blog_management.urls')),
    path('faq_management/', include('faq_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)