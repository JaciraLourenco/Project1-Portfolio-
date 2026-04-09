import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

with open('files/curso_lig.json', encoding='utf-8') as f:
    dados = json.load(f)

lic = Licenciatura.objects.first()
if not lic:
    print("❌ Nenhuma Licenciatura encontrada! Cria primeiro a Licenciatura no admin.")
    exit()

print(f"✅ Licenciatura encontrada: {lic.nome}")

ucs = dados.get('courseFlatPlan', [])
print(f"\nA carregar {len(ucs)} UCs...")

count_criadas = 0
count_existentes = 0

for uc in ucs:
    nome = uc.get('curricularUnitName', '')
    ano = uc.get('curricularYear', 1)
    semestre = uc.get('term', 1)
    codigo = uc.get('curricularIUnitReadableCode', '')

    if nome:
        obj, created = UnidadeCurricular.objects.get_or_create(
            nome=nome,
            defaults={
                'licenciatura': lic,
                'ano': ano,
                'semestre': semestre if semestre in [1, 2] else 1,
                'descricao': f"Código: {codigo}",
            }
        )
        if created:
            count_criadas += 1
            print(f"✅ criada - {nome}")
        else:
            count_existentes += 1
            print(f"⚠️  já existe - {nome}")

print(f"\n🎉 Concluído! {count_criadas} criadas, {count_existentes} já existiam.")