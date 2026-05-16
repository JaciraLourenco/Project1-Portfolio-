import os
from django.core.files import File

from escola.models import Curso
from portfolio.models import Evento, MakingOf, Projeto, Tecnologia, UnidadeCurricular, Formacao
from artigos.models import Artigo

MEDIA_ROOT = '/workspaces/Project1-Portfolio-/media'

modelos = [
    (Curso, 'imagem'),
    (Evento, 'imagem'),
    (Evento, 'certificado'),
    (MakingOf, 'foto'),
    (Projeto, 'imagem'),
    (Tecnologia, 'logo'),
    (UnidadeCurricular, 'imagem'),
    (Formacao, 'certificado'),
    (Artigo, 'fotografia'),
]

for modelo, campo in modelos:
    for obj in modelo.objects.all():
        field = getattr(obj, campo)
        if field and field.name:
            local_path = os.path.join(MEDIA_ROOT, field.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    getattr(obj, campo).save(
                        os.path.basename(local_path),
                        File(f),
                        save=True
                    )
                print(f"Migrado: {obj} - {campo}")
            else:
                print(f"Ficheiro não encontrado: {local_path}")