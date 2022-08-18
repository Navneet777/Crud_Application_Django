from django.urls import path
from .views import AdminLogin,LogoutView

urlpatterns = [
    path('', AdminLogin.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout")
    ]




