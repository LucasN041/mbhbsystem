from django import forms
from .models import Treinamentos

class TreinamentosFormCadastro(forms.ModelForm):
    class Meta:
        model = Treinamentos
        fields = ['titulo', 'topico1', 'texto1', 'topico2', 'texto2', 'topico3', 'texto3',
                  'topico4', 'texto4','topico5', 'texto5','topico6', 'texto6','topico7', 'texto7',]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'topico1': forms.TextInput(attrs={'class': 'form-control'}),
            'texto1': forms.Textarea(attrs={'class': 'form-control'}),
            'topico2': forms.TextInput(attrs={'class': 'form-control'}),
            'texto2': forms.Textarea(attrs={'class': 'form-control'}),
            'topico3': forms.TextInput(attrs={'class': 'form-control'}),
            'texto3': forms.Textarea(attrs={'class': 'form-control'}),
            'topico4': forms.TextInput(attrs={'class': 'form-control'}),
            'texto4': forms.Textarea(attrs={'class': 'form-control'}),
            'topico5': forms.TextInput(attrs={'class': 'form-control'}),
            'texto5': forms.Textarea(attrs={'class': 'form-control'}),
            'topico6': forms.TextInput(attrs={'class': 'form-control'}),
            'texto6': forms.Textarea(attrs={'class': 'form-control'}),
            'topico7': forms.TextInput(attrs={'class': 'form-control'}),
            'texto7': forms.Textarea(attrs={'class': 'form-control'}),
        }