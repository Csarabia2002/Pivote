from django import forms
from .models import OfertaTrabajo

class OfertaTrabajoForm(forms.ModelForm):
    class Meta:
        model = OfertaTrabajo
        fields = ['titulo', 'descripcion',]