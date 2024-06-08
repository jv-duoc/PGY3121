from django import forms

class NuevaTareaForm(forms.Form):
    texto = forms.CharField( max_length=1024, required=True,min_length=8)
    completado = forms.BooleanField(required=False)


class RegistroForm(forms.Form):
    usuario = forms.EmailField(max_length=64,required=True)
    password = forms.CharField(label='Contraseña',required=True,widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña',required=True,widget=forms.PasswordInput)