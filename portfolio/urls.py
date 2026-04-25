from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='portfolio'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('eventos/', views.eventos_view, name='eventos'),
    path('makingof/', views.makingof_view, name='makingof'),
]