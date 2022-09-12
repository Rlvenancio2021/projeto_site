from django.db import models

# Create your models here.
class Curso(models.Model):
    STATUS = (
        ('C','Concluído'),
        ('E','Estudando'),
        ('S','Suspenso')
    )
    CATEGORIA = (
        ('P','Presencial'),
        ('D','Distância')
    )
    AREA_ESTUDO = (
        ('F','Finanças'),
        ('T','Tecnologia da Informação'),
        ('O','Outros')
    )
    nome_instituicao = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='E')
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, null=False, default='D')
    area_estudo = models.CharField(max_length=1, choices=AREA_ESTUDO, blank=False, null=False)
    linguagem = models.CharField(max_length=50, default="Não se aplica")
    nome_curso = models.CharField(max_length=200)
    tecnologia = models.TextField(blank=True, null=True)
    inicio = models.DateField(blank=True, null=True)
    conclusao = models.DateField(blank=True, null=True)
    carga_horaria = models.IntegerField()
    url_certificado = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.nome_curso