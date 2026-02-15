from django import forms
from .models import Curriculo
from django.forms import inlineformset_factory
from .models import Curriculo, Experiencia, Formacao, Habilidade, Idioma, Certificado

class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo 
        fields = [
            'titulo', 'nome_completo', 'email', 'telefone',
            'linkedin_url', 'github_url', 'cidade', 'estado',
            'resumo_profissional'
        ]

ExperienciaFormSet = inlineformset_factory(
    Curriculo, Experiencia,
    fields=['cargo', 'empresa', 'data_inicio', 'data_fim', 'descricao'],
    extra=0, can_delete=True
)
FormacaoFormSet = inlineformset_factory(
    Curriculo, Formacao,
    fields=['instituicao', 'curso', 'nivel_de_escolaridade', 'data_inicio', 'data_fim'],
    extra=0, can_delete=True
)
HabilidadeFormSet = inlineformset_factory(
    Curriculo, Habilidade,
    fields=['nome_tecnico', 'nivel'],
    extra=0, can_delete=True
)

IdiomaFormSet = inlineformset_factory(
    Curriculo, Idioma,
    fields=['nome', 'nivel'],
    extra=0, can_delete=True
)
CertificadoFormSet = inlineformset_factory(
    Curriculo, Certificado,
    fields=['nome', 'organizacao_emissora', 'data_emissao', 'link_validacao'],
    extra=0, can_delete=True
)