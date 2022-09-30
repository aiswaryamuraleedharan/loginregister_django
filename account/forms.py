from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisterDetails
        fields = '__all__'
