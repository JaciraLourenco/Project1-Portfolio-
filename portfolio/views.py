from django.shortcuts import render, redirect, get_object_or_404
from .models import (Licenciatura, Projeto, Tecnologia, TFC,
                     Competencia, Formacao, MakingOf, Evento)
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

def index_view(request):
    return render(request, 'portfolio/index.html')

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('unidades').all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias_usadas').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def projeto_criar_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Novo Projeto'})

def projeto_editar_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Editar Projeto'})

def projeto_apagar_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_confirmar_apagar.html', {'projeto': projeto})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.prefetch_related('projetos').all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def tecnologia_criar_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm()
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Nova Tecnologia'})

def tecnologia_editar_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Editar Tecnologia'})

def tecnologia_apagar_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_confirmar_apagar.html', {'tecnologia': tecnologia})

def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('projetos', 'tecnologias').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def competencia_criar_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Nova Competência'})

def competencia_editar_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Editar Competência'})

def competencia_apagar_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_confirmar_apagar.html', {'competencia': competencia})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def formacao_criar_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm()
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Nova Formação'})

def formacao_editar_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Editar Formação'})

def formacao_apagar_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_confirmar_apagar.html', {'formacao': formacao})

def eventos_view(request):
    eventos = Evento.objects.all()
    return render(request, 'portfolio/eventos.html', {'eventos': eventos})

def makingof_view(request):
    makingof = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingof': makingof})
