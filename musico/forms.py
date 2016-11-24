from django.forms import ModelForm
from django.core.files import File as FileWrapper
from django import forms
from .models import Musico, Album,Cometario

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ('nombre', 'apellido', 'instrumento','fecha_nacimiento','direccion','telefono','correo')

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('titulo', 'musico', 'fecha_lanzamiento','favorito','descripcion','foto',)

class CometarioForm(forms.ModelForm):
    class Meta:
        model = Cometario
        fields = ('cometario',)
