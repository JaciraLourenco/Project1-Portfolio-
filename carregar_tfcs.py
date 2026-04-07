import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import TFC

with open('tfcs_deisi_2024_2025.json', encoding='utf-8') as f:
    dados = json.load(f)

tfcs = dados['tfcs']
count = 0

for tfc in tfcs:
    TFC.objects.get_or_create(
        titulo=tfc.get('titulo', ''),
        defaults={
            'autores': ', '.join(tfc.get('autores', [])),
            'orientadores': ', '.join(tfc.get('orientadores', [])),
            'licenciatura': ', '.join(tfc.get('licenciaturas', [])),
            'resumo': tfc.get('resumo', ''),
            'palavras_chave': ', '.join(tfc.get('palavras_chave', [])),
            'areas': ', '.join(tfc.get('areas', [])),
            'tecnologias': ', '.join(tfc.get('tecnologias', [])),
            'ano': tfc.get('ano', ''),
            'imagem_url': tfc.get('imagem', ''),
            'link_pdf': tfc.get('link_pdf', ''),
            'email': tfc.get('email', ''),
            'classificacao_interesse': tfc.get('rating', 2),
        }
    )
    count += 1
    print(f"✅ {count} - {tfc.get('titulo', '')[:60]}")

print(f"\n🎉 {count} TFCs carregados com sucesso!")