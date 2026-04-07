from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular
from .models import Licenciatura, UnidadeCurricular, Projeto
from .models import Licenciatura, UnidadeCurricular, Projeto, Tecnologia
from .models import Licenciatura, UnidadeCurricular, Projeto, Tecnologia, TFC

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'area', 'duracao_anos')
    search_fields = ('nome', 'instituicao')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'licenciatura', 'ano', 'semestre')
    search_fields = ('nome', 'docente_nome')
    list_filter = ('ano', 'semestre', 'licenciatura')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_curricular', 'data')
    search_fields = ('nome', 'tecnologias')
    list_filter = ('unidade_curricular',)   

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_interesse')
    search_fields = ('nome',)
    list_filter = ('categoria', 'nivel_interesse')

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'ano', 'classificacao_interesse')
    search_fields = ('titulo', 'autores')
    list_filter = ('ano', 'classificacao_interesse')