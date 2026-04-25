from django.shortcuts import render
from .models import (Licenciatura, Projeto, Tecnologia, TFC,
                     Competencia, Formacao, MakingOf, Evento)

def index_view(request):
    return render(request, 'portfolio/index.html')

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('unidades').all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias_usadas').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.prefetch_related('projetos').all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('projetos', 'tecnologias').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def eventos_view(request):
    eventos = Evento.objects.all()
    return render(request, 'portfolio/eventos.html', {'eventos': eventos})

def makingof_view(request):
    makingof = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingof': makingof})