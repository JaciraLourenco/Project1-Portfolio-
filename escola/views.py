from django.shortcuts import render
from .models import Curso
from .models import Professor

def cursos_view(request):

    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def professores_view(request):

    professores = Professor.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'escola/cursos.html', {'cursos': cursos})