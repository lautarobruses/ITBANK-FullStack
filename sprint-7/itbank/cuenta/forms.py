from django import forms

class RegisterForm(forms.Form):
    name_surname = forms.CharField(label='Nombre y Apellido:', max_length=100, required=True, widget=forms.TextInput())
    password = forms.CharField(label='Contraseña:', required=True, widget=forms.PasswordInput)
    dni = forms.IntegerField(label='DNI:', required=True, widget=forms.TextInput())
    mail = forms.EmailField(label='Correo Electrónico:', required=True, widget=forms.EmailInput())
    confirm_password = forms.CharField(label='Confirmar Contraseña:', required=True, widget=forms.PasswordInput())
    phone = forms.IntegerField(label='Teléfono:', required=True, widget=forms.TextInput())
    checkbox = forms.BooleanField(label='Acepto los Términos y Condiciones', required=True)
