from django import forms
from .models import Requerimento
from django.contrib.auth.models import Group
from users.models import CustomUser

class AdicionarUsuarioGrupoForm(forms.Form):
    usuario = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.filter(
            name__in=['praça', 'rh', 'depensino']
        ),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class RequerimentoForm(forms.ModelForm):
    class Meta:
        model = Requerimento
        fields = ['opcoes', 'solicitante', 'militar',]
    
        widgets = {
            'opcoes': forms.Select(attrs={'class': 'form-control'}),
            'solicitante': forms.Select(attrs={'class': 'form-control'}),
            'militar': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RequerimentoFormRH(forms.ModelForm):
    class Meta:
        model = Requerimento
        fields = ['opcoes', 'solicitante', 'militar', 'status',]
    
        widgets = {
            'opcoes': forms.Select(attrs={'class': 'form-control'}),
            'solicitante': forms.Select(attrs={'class': 'form-control'}),
            'militar': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }