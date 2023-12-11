import requests
import json 

api_url = "http://instituto.islagaia.pt/ws/wsCambio.asmx/cambioUSD"

response = requests.get(api_url)

if response.status_code == 200:
	try:
 		data = response.json()
		valor_cambio = data["value"]

		print (f"Valor do câmbio:
{valor_cambio}")
	except json.JSONDecodeError:
	print ("Erro ao descodificar a resposta JSON.")
else:
	print (f"Falha na solicitação à API.Código de status: {response.status_code}")
