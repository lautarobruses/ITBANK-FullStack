from django import forms
from django.core.exceptions import ValidationError

class FormularioCalculadoraPrestamos(forms.Form):
    monto = forms.DecimalField(label='Monto del préstamo', max_digits=12, decimal_places=2)
    tasa_interes = forms.DecimalField(label='Tasa de interés (anual, en %)', max_digits=5, decimal_places=2)
    meses = forms.IntegerField(label='Duración del préstamo (en meses)')

    def clean_tasa_interes(self):
        tasa_interes = self.cleaned_data.get('tasa_interes')
        if tasa_interes == 0:
            raise ValidationError('La tasa de interés no puede ser cero.')
        return tasa_interes

    def clean_meses(self):
        meses = self.cleaned_data.get('meses')
        if meses == 0:
            raise ValidationError('El mes no puede ser cero.')
        return meses

class SolicitudPrestamoForm(forms.Form):
    TIPOS_PRESTAMO = [
        ('hipotecario', 'Hipotecario'),
        ('prendario', 'Prendario'),
        ('personal', 'Personal'),
    ]
    tipo_prestamo = forms.ChoiceField(choices=TIPOS_PRESTAMO, label='Tipo de préstamo')
    monto_solicitado = forms.DecimalField(max_digits=9, decimal_places=2, label='Monto solicitado')
    fecha_prestamo = forms.DateField(label='Fecha del préstamo')
