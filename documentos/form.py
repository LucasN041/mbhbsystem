from django import forms
from .models import Documentos

class DocumentosFormCadastro(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['titulo', 'texto1',]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'texto1': forms.Textarea(attrs={'class': 'form-control'}),
        }