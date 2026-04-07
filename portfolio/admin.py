from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'area', 'duracao_anos')
    search_fields = ('nome', 'instituicao')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'licenciatura', 'ano', 'semestre')
    search_fields = ('nome', 'docente_nome')
    list_filter = ('ano', 'semestre', 'licenciatura')