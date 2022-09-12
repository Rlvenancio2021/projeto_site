from django.db import models

# Create your models here.
class Graduacao(models.Model):
    NIVEL = (
        ('G', 'Graduação'),
        ('P', 'Pós_Graduação'),
        ('O', 'Outros')
    )
    STATUS = (
        ('C','Concluído'),
        ('E','Estudando'),
        ('S','Suspenso')
    )
    CATEGORIA = (
        ('P','Presencial'),
        ('D','Distância')
    )
    nome_instituicao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=True, null=True,)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='E')
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, null=False, default='D')
    nome_curso = models.CharField(max_length=50)
    inicio = models.DateField()
    conclusao = models.DateField()
    
    def __str__(self):
        return self.nome_curso