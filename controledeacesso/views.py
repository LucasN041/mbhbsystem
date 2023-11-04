from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .form import LoginForm, CustomPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


class LoginViewModificada(LoginView):
    template_name = 'templates/login.html'
    authentication_form = LoginForm

class AlterarSenhaView(GroupRequiredMixin,LoginRequiredMixin,PasswordChangeView):
    group_required = [u"praça", u"oficial"]
    template_name = 'templates/config.html'  
    success_url = reverse_lazy('config')  
    form_class = CustomPasswordChangeForm
