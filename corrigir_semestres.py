import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import UnidadeCurricular

semestres = {
    # 1º Ano - Semestre 1
    'Contabilidade': 1,
    'Fundamentos de Sistemas de Informação': 1,
    'Matemática I': 1,
    'Teoria e Prática de Marketing': 1,
    # 1º Ano - Semestre 2
    'Algoritmia e Estruturas de Dados': 2,
    'Cálculo Financeiro': 2,
    'Competências Comportamentais': 2,
    'Fundamentos de Programação': 2,
    'Linguagens de Programação I': 2,
    'Matemática II': 2,
    'Métricas Empresariais': 2,
    # 2º Ano - Semestre 1
    'Bases de Dados': 1,
    'Direito Informático': 1,
    'Instrumentos de Gestão': 1,
    'Motivação e Liderança': 1,
    'Programação Low-Code e No-Code': 1,
    'Sistemas Operativos': 1,
    # 2º Ano - Semestre 2
    'Engenharia de Requisitos e Testes': 2,
    'Gestão Financeira': 2,
    'Programação Web': 2,
    'Redes de Computadores': 2,
    'Sistemas de Suporte à Decisão': 2,
    # 3º Ano - Anual
    'Trabalho Final de Curso': 1,
    # 3º Ano - Semestre 1
    'Data Mining': 1,
    'Engenharia de Software': 1,
    'Interação Humano-Máquina': 1,
    'Sistemas Móveis Empresariais': 1,
    # 3º Ano - Semestre 2
    'Auditoria de Sistemas de Informação': 2,
    'Controlo de Gestão': 2,
    'Gestão de Projetos': 2,
    'Inteligência Artificial': 2,
    'Sistemas de Informação na Nuvem': 2,
}

print("A corrigir semestres...")
count = 0
for nome, semestre in semestres.items():
    updated = UnidadeCurricular.objects.filter(nome=nome).update(semestre=semestre)
    if updated:
        print(f"✅ {nome} → Semestre {semestre}")
        count += 1
    else:
        print(f"⚠️  Não encontrada: {nome}")

print(f"\n🎉 {count} UCs atualizadas!")