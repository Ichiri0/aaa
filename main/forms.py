import django.forms

from .models import User
from django.forms import ModelForm, TextInput, IntegerField, EmailField

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'name', 'middle_name', 'email', 'phone']
        widgets = {
            'last_name': TextInput(attrs={
                'class': 'class_nameSHABLON',
                'placeholder': 'Фамилия'
            }),
            'name': TextInput(attrs={
                'class': 'class_nameSHABLON',
                'placeholder': 'Имя'
            }),
            'middle_name': TextInput(attrs={
                'class': 'class_nameSHABLON',
                'placeholder': 'Отчество'
            }),
            'email': django.forms.EmailInput(attrs={
                'class': 'class_nameSHABLON',
                'placeholder': 'Электронная почта'
            }),
            'phone': django.forms.TextInput(attrs={
                'class': 'class_nameSHABLON',
                'placeholder': 'Номер Телефона'
            }),
        }