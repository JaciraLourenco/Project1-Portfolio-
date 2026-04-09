import os
import django
import requests
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

schoolYear = '202526'
course = 12  # LIG

os.makedirs('files', exist_ok=True)

# Descarregar info do curso
url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
payload = {'language': 'PT', 'courseCode': course, 'schoolYear': schoolYear}
headers = {'content-type': 'application/json'}

print("A descarregar informação do curso...")
response = requests.post(url, json=payload, headers=headers)
dados = response.json()

# Guardar JSON
with open('files/curso_lig.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print("✅ JSON do curso guardado em files/curso_lig.json")

# Atualizar a Licenciatura na BD
lic = Licenciatura.objects.first()
if lic:
    print(f"Licenciatura encontrada: {lic.nome}")

# Carregar UCs do plano curricular
ucs = dados.get('courseFlatPlan', [])
print(f"\nA carregar {len(ucs)} UCs...")

for uc in ucs:
    nome = uc.get('curricularUnitName', '')
    ano = uc.get('curricularYear', 1)
    semestre = uc.get('term', 1)
    codigo = uc.get('curricularIUnitReadableCode', '')

    if lic and nome:
        obj, created = UnidadeCurricular.objects.get_or_create(
            nome=nome,
            defaults={
                'licenciatura': lic,
                'ano': ano,
                'semestre': semestre if semestre in [1, 2] else 1,
                'descricao': f"Código: {codigo}",
            }
        )
        status = "✅ criada" if created else "⚠️ já existe"
        print(f"{status} - {nome}")

print("\n🎉 Concluído!")