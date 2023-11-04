from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Senha antiga',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='Nova senha',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirmar nova senha',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nickname',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

