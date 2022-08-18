from django.shortcuts import render ,redirect, reverse
from django.contrib.auth.models import User , auth
from django.contrib import messages

from django.contrib.auth.views import LoginView    

class AdminLogin(LoginView):
    template_name = 'authentication/Login_View_form.html'