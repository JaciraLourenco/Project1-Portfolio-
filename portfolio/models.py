from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    duracao_anos = models.IntegerField()
    descricao = models.TextField(blank=True)
    link = models.URLField(blank=True)
    
    def __str__(self):
        return self.nome