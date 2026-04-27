from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='portfolio'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/novo/', views.projeto_criar_view, name='projeto_criar'),
    path('projetos/<int:id>/editar/', views.projeto_editar_view, name='projeto_editar'),
    path('projetos/<int:id>/apagar/', views.projeto_apagar_view, name='projeto_apagar'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologias/novo/', views.tecnologia_criar_view, name='tecnologia_criar'),
    path('tecnologias/<int:id>/editar/', views.tecnologia_editar_view, name='tecnologia_editar'),
    path('tecnologias/<int:id>/apagar/', views.tecnologia_apagar_view, name='tecnologia_apagar'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencias/novo/', views.competencia_criar_view, name='competencia_criar'),
    path('competencias/<int:id>/editar/', views.competencia_editar_view, name='competencia_editar'),
    path('competencias/<int:id>/apagar/', views.competencia_apagar_view, name='competencia_apagar'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacoes/novo/', views.formacao_criar_view, name='formacao_criar'),
    path('formacoes/<int:id>/editar/', views.formacao_editar_view, name='formacao_editar'),
    path('formacoes/<int:id>/apagar/', views.formacao_apagar_view, name='formacao_apagar'),
    path('eventos/', views.eventos_view, name='eventos'),
    path('makingof/', views.makingof_view, name='makingof'),
]
