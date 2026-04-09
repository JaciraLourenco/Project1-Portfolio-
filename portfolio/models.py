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

class Tecnologia(models.Model):
    NIVEL_CHOICES = [
        (1, '⭐ Iniciante'),
        (2, '⭐⭐ Básico'),
        (3, '⭐⭐⭐ Intermédio'),
        (4, '⭐⭐⭐⭐ Avançado'),
        (5, '⭐⭐⭐⭐⭐ Expert'),
    ]
    
    CATEGORIA_CHOICES = [
        ('linguagem', 'Linguagem de Programação'),
        ('framework', 'Framework'),
        ('base_dados', 'Base de Dados'),
        ('ferramenta', 'Ferramenta'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link_oficial = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES, default=3)
    projetos = models.ManyToManyField(Projeto, blank=True, related_name='tecnologias_usadas')

    def __str__(self):
        return self.nome

class TFC(models.Model):
    INTERESSE_CHOICES = [
        (1, '⭐ Pouco interessante'),
        (2, '⭐⭐ Interessante'),
        (3, '⭐⭐⭐ Muito interessante'),
    ]

    titulo = models.CharField(max_length=500)
    autores = models.TextField()
    orientadores = models.TextField(blank=True)
    licenciatura = models.CharField(max_length=300, blank=True)
    resumo = models.TextField(blank=True)
    palavras_chave = models.TextField(blank=True)
    areas = models.TextField(blank=True)
    tecnologias = models.TextField(blank=True)
    ano = models.CharField(max_length=10, blank=True)
    imagem_url = models.URLField(blank=True)
    link_pdf = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    classificacao_interesse = models.IntegerField(choices=INTERESSE_CHOICES, default=2)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    TIPO_CHOICES = [
        ('tecnica', 'Técnica'),
        ('soft', 'Soft Skill'),
        ('linguistica', 'Linguística'),
        ('outra', 'Outra'),
    ]

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    projetos = models.ManyToManyField(Projeto, blank=True, related_name='competencias')
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='competencias')

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    TIPO_CHOICES = [
        ('academica', 'Académica'),
        ('curso', 'Curso Online'),
        ('certificacao', 'Certificação'),
        ('workshop', 'Workshop'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    em_curso = models.BooleanField(default=False)
    certificado = models.FileField(upload_to='certificados/', blank=True, null=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return f"{self.nome} - {self.instituicao}"

class MakingOf(models.Model):
    TIPO_CHOICES = [
        ('decisao', 'Decisão de Modelação'),
        ('erro', 'Erro e Correção'),
        ('diagrama', 'Diagrama/Esquema'),
        ('foto', 'Foto do Caderno'),
        ('ia', 'Uso de IA'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='makingof/', blank=True, null=True)
    data = models.DateField(auto_now_add=True)
    entidade_relacionada = models.CharField(max_length=100, blank=True, help_text="Ex: Licenciatura, Projeto, TFC...")

    class Meta:
        ordering = ['-data']
        verbose_name = 'Making Of'
        verbose_name_plural = 'Making Of'

    def __str__(self):
        return f"{self.tipo} - {self.titulo}"


class Evento(models.Model):
    TIPO_CHOICES = [
        ('conferencia', 'Conferência'),
        ('workshop', 'Workshop'),
        ('seminario', 'Seminário'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    local = models.CharField(max_length=200, blank=True)
    data = models.DateField()
    link = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)
    certificado = models.FileField(upload_to='eventos/certificados/', blank=True, null=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f"{self.nome} ({self.tipo})"