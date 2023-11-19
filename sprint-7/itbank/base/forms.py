from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, widget=forms.TextInput())
    email = forms.EmailField(label='Correo Electrónico', required=True, widget=forms.EmailInput())
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea())
