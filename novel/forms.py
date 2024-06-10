from django import forms
from .models import Autor, Novela, Recenze

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['jmeno', 'prijmeni', 'datum_narozeni']

class NovelaForm(forms.ModelForm):
    class Meta:
        model = Novela
        fields = ['nazev', 'autor', 'datum_vydani']

class RecenzeForm(forms.ModelForm):
    class Meta:
        model = Recenze
        fields = ['obsah', 'hodnoceni']
