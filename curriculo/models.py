from django.db import models
from django.contrib.auth.models import User


class Curriculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100, help_text="Ex: Currículo para Vaga Python")
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=30)
    linkedin_url = models.URLField(blank=True, null=True) #não é obrigatório
    github_url = models.URLField(blank=True, null=True) 
    cidade = models.CharField(max_length=300)
    estado = models.CharField(max_length=300)
    resumo_profissional = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.titulo} - {self.nome_completo}"
    
class Experiencia(models.Model):
    curriculo = models.ForeignKey(Curriculo,on_delete=models.CASCADE, related_name='experiencias')
    cargo = models.CharField(max_length=300)
    empresa = models.CharField(max_length=300)
    data_inicio = models.DateField()
    data_fim = models.DateField (null=True,blank=True)
    descricao = models.TextField(help_text="Descreva suas atividades e conquistas.")
    def __str__(self):
        return f"{self.cargo} em {self.empresa}"


class Formacao(models.Model):
    NIVEL_CHOICES = (
        ('TEC', 'Tecnólogo'),
        ('BAC', 'Bacharelado'),
        ('LIC', 'Licenciatura'),
        ('MES', 'Mestrado'),
        ('DOC', 'Doutorado'),
        ('POS', 'Pós-Graduação/MBA'),
    )
    curriculo = models.ForeignKey(Curriculo,on_delete=models.CASCADE, related_name='formacoes')
    instituicao = models.CharField(max_length=300)
    curso = models.CharField(max_length=300)
    nivel_de_escolaridade = models.CharField(max_length=3,choices=NIVEL_CHOICES)
    data_inicio = models.DateField()
    data_fim = models.DateField (null=True,blank=True)
    def __str__(self):
        return f"{self.curso} em {self.instituicao}"

class Habilidade(models.Model):
    PROF_CHOICES = (
        ("BAS", "Básico"),
        ("INT", "Intermediário"),
        ("AVA", "Avançado"),
        ("PRO", "Profissional"),
    )
    curriculo = models.ForeignKey(Curriculo,on_delete=models.CASCADE, related_name='habilidades')
    nome_tecnico = models.CharField(max_length=200)
    nivel = models.CharField(max_length=3,choices=PROF_CHOICES)
    def __str__(self):
        return f"{self.nome_tecnico} ({self.get_nivel_display()})"
    
class Idioma(models.Model):
    NIVEL_CHOICES = (
        ('BAS', 'Básico'),
        ('INT', 'Intermediário'),
        ('AVA', 'Avançado'),
        ('FLU', 'Fluente'),
        ('NAT', 'Nativo'),
    )

    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, related_name='idiomas')
    nome = models.CharField(max_length=100, help_text="Ex: Inglês, Espanhol, Francês")
    nivel = models.CharField(max_length=3, choices=NIVEL_CHOICES)

    def __str__(self):
        return f"{self.nome} - {self.get_nivel_display()}"
    
class Certificado(models.Model):
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, related_name='certificados')
    
    nome = models.CharField(max_length=200, help_text="Ex: AWS Cloud Practitioner")
    organizacao_emissora = models.CharField(max_length=200, help_text="Ex: Amazon, Google, Alura")
    
    data_emissao = models.DateField()
    
    # Campo opcional, mas muito valorizado
    link_validacao = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.organizacao_emissora})"

