from django import forms

class NuevaTareaForm(forms.Form):
    texto = forms.CharField( max_length=1024, required=True,min_length=8)
    completado = forms.BooleanField(required=False)