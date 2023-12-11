import requests

# URL da API
url = "https://api.currencylayer.com/live?access_key=ghp_MZCqcrZ733KW71jR5GUOBzc46S0IMYOCVF3D&currencies=USD,EUR"

# Faz a requisição à API
r = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if r.status_code == 200:

    # Obtém os dados da API
    dados = r.json()

    # Obtém o valor do câmbio
    cambio = dados.get("quotes", {}).get("USDEUR")

    # Imprime o resultado
    print("Cambio USD:", cambio)

else:
    print("Erro na requisição")
