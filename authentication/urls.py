from django.urls import path
from .views import AdminLogin

urlpatterns = [
    path('', AdminLogin.as_view(), name="login")
    ]




