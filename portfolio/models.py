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

class UnidadeCurricular(models.Model):
    SEMESTRE_CHOICES = [
        (1, 'Semestre 1'),
        (2, 'Semestre 2'),
    ]

    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='unidades')
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='unidades/', blank=True, null=True)
    docente_nome = models.CharField(max_length=200, blank=True)
    docente_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nome} ({self.ano}º ano)"


class Projeto(models.Model):
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True, related_name='projetos')
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    tecnologias = models.TextField(help_text="Ex: Python, Django, HTML, CSS")
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text="Link para video demo no YouTube")
    link_github = models.URLField(blank=True)
    data = models.DateField(blank=True, null=True)
    conceitos_aplicados = models.TextField(blank=True, help_text="Conceitos da UC aplicados neste projeto")

    def __str__(self):
        return self.nome