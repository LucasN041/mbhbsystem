from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = fields = '__all__'



class EditFormUser(forms.ModelForm):
    PATENTE_CHOICES = CustomUser.PATENTES[:7] 
    patente = forms.ChoiceField(
        choices=PATENTE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['patente', 'status', 'datapromo', 'responsavel', 'status']

        widgets = {
            'datapromo': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class RegistrationFormRH(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    PATENTE_CHOICES = CustomUser.PATENTES[:7] 
    patente = forms.ChoiceField(
        choices=PATENTE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username','patente', 'status', 'datapromo', 'responsavel', 'status']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'datapromo': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }