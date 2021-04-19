from django import forms

from .models import Bank


class CreateBankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ('name', 'balance')

