from django import forms
from api.models import StatusSenha, Tipo, Categoria, Guiche, Campus, Atendente

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = StatusSenha
        fields = [
            'nome'
        ]


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = [
            'nome'
        ]

class StatusForm(forms.ModelForm):
    class Meta:
        model = StatusSenha
        fields = [
            'nome'
        ]

class GuicheForm(forms.ModelForm):
    class Meta:
        model = Guiche
        fields = [
            'num_guiche','status'
        ]

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = [
            'Campo'
        ]

class AtendenteForm(forms.ModelForm):
    class Meta:
        model = Atendente
        fields = [
            'Siape','Nome'
        ]