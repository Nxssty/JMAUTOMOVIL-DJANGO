from django import forms
from django.forms import inlineformset_factory
from .models import Autos, Imagen

class AutoForm(forms.ModelForm):
    class Meta:
        model = Autos
        fields = ['marca', 'modelo', 'cilindrada', 'anio', 'transmision', 'kilometraje', 'combustible', 'descripcion', 'precio', 'vendido', 'recien_llegado']

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen']

ImagenFormSet = inlineformset_factory(Autos, Imagen, form=ImagenForm, extra=4)
