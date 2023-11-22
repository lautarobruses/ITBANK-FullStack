from django import forms

class TransferForm(forms.Form):
    beneficiario = forms.CharField(max_length=100)
    monto = forms.DecimalField()