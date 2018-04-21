from django.contrib.auth.views import LoginView
from django.shortcuts import render


login = LoginView.as_view(template_name='login.html')
