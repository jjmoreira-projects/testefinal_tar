# Importar bibliotecas necessárias
import requests

# Invocar API
r = requests.get("http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa")

# Verificar se a resposta é válida
if r.status_code != 200:
    print("Erro ao invocar API")
    sys.exit(1)

# Decodificar resposta
data = r.json()

# Imprimir resultado
print(f"Número sorteado: {data['Numero']}")
print(f"Série sorteada: {data['Serie']}")
