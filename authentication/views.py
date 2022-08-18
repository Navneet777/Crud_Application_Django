from django.shortcuts import render ,redirect, reverse
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView   
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
class AdminLogin(LoginView):
    template_name = 'authentication/Login_View_form.html'

class LogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)