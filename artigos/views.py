from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

def artigos_view(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/artigos.html', {'artigos': artigos})

def artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = artigo.comentarios.all()
    form_comentario = ComentarioForm()
    return render(request, 'artigos/artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
    })

@login_required
def artigo_criar_view(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigo', id=artigo.id)
    else:
        form = ArtigoForm()
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Novo Artigo'})

@login_required
def artigo_editar_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('artigos')
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigo', id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Editar Artigo'})

@login_required
def artigo_apagar_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('artigos')
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos')
    return render(request, 'artigos/artigo_confirmar_apagar.html', {'artigo': artigo})

@login_required
def artigo_like_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigo', id=artigo.id)

@login_required
def artigo_comentar_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
    return redirect('artigo', id=artigo.id)