# -*- encoding: utf-8 -*-
from hacktrick.models import Domain
from django.forms import TextInput
from django.forms.models import ModelForm


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