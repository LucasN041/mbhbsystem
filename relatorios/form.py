from django import forms
from .models import Relatorios


class RelatoriosFormCadastro(forms.ModelForm):
    class Meta:
        model = Relatorios
        fields = ['treinamento', 'sala', 'responsavel', 'data1', 'treinador', 'aprovados', 'reprovados',
                  'data2', 'observações',]
    
        widgets = {
            'treinamento': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.Select(attrs={'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'}),
            'data1': forms.TextInput(attrs={'class': 'form-control'}),
            'treinador': forms.Select(attrs={'class': 'form-control'}),
            'aprovados': forms.Textarea(attrs={'class': 'form-control'}),
            'reprovados': forms.Textarea(attrs={'class': 'form-control'}),
            'data2': forms.TextInput(attrs={'class': 'form-control'}),
            'observações': forms.Textarea(attrs={'class': 'form-control'}),
        }

class RelatoriosOfcFormCadastro(forms.ModelForm):
    class Meta:
        model = Relatorios
        fields = ['treinamento', 'sala', 'responsavel', 'data1', 'treinador', 'aprovados', 'reprovados',
                  'data2', 'observações', 'status',]
    
        widgets = {
            'treinamento': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.Select(attrs={'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'}),
            'data1': forms.TextInput(attrs={'class': 'form-control'}),
            'treinador': forms.Select(attrs={'class': 'form-control'}),
            'aprovados': forms.Textarea(attrs={'class': 'form-control'}),
            'reprovados': forms.Textarea(attrs={'class': 'form-control'}),
            'data2': forms.TextInput(attrs={'class': 'form-control'}),
            'observações': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }