from django.db import models
from django.contrib.auth.models import User


class Curriculo(models.model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
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
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.titulo} - {self.nome_completo}"
