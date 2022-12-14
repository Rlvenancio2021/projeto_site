from django.db import models

# Create your models here.
class Carreira(models.Model):
    nome_empresa_fonetico = models.CharField(max_length=20)
    nome_empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    funcao = models.TextField()
    inicio = models.DateField()
    fim = models.DateField()
    empresa_atual = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_empresa_fonetico
    
class Resumo_Carreira(models.Model):
    titulo = models.CharField(max_length=100)
    resumo = models.TextField()
    data_inclusao = models.DateField()
    data_modificacao = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo