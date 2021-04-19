from django import forms

from src.debts.models import Operation


class CreateOperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ('bank', 'type', 'amount', 'date', 'category', 'description')
