from django import forms


class RegistroForm(forms.Form):
    username = forms.CharField( label='Usuario', max_length=100, widget=forms.TextInput(
        attrs={
            'placeholder':'Ingrese su Usuario'
        }))
    nombres = forms.CharField(label='Nombres', max_length=120, widget=forms.TextInput(
        attrs={
            'placeholder':'Ingrese sus nombres completos'
        }))
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'placeholder':'Ingrese su contraseña',
            'id' : 'password',
            'requires' : 'requires'
        }))
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento',widget=forms.TextInput(
        attrs={
            'type':'date'
        }))
    

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ingrese su Usuario'}
    ))
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={'placeholder': 'Ingrese su contraseña'}
    ))