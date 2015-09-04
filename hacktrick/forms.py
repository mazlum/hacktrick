# -*- encoding: utf-8 -*-
from hacktrick.models import Domain
from django.forms import TextInput, CharField, PasswordInput
from django.forms.models import ModelForm
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = CharField(label="Kullanıcı Adı",
                         widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı adı'}))
    password = CharField(label="Şifre",
                         widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'}))


class DomainForm(ModelForm):
    class Meta:
        model = Domain
        fields = ['domain']

        widgets = {
            'domain': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Domain giriniz.'}),
        }

        labels = {
            'domain': 'Domain'
        }

        error_messages = {
            'domain': {'required': 'Bu alan zorunludur.', 'invalid': 'Geçersiz değer.'}
        }