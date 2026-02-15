from django import forms
from .models import curriculo

class CurriculoForm(forms.ModelForm):
    class meta:
        model = Curriculo 
        fields = [
            'titulo', 'nome_completo', 'email', 'telefone',
            'linkedin_url', 'github_url', 'cidade', 'estado',
            'resumo_profissional'
        ]

