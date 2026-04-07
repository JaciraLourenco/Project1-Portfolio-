from django.contrib import admin
from .models import Licenciatura

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'area', 'duracao_anos')
    search_fields = ('nome', 'instituicao')