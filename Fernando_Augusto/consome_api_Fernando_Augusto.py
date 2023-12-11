import requests
import xml.etree.ElementTree as ET

def consome_api():
    url = "http://instituto.islagaia.pt/ws/wscambio.asmx/cambioUSD"

    response = requests.get(url)
    
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        numero_sorteio = root.text
        return numero_sorteio
    else:
        return None

cambioUSD = consome_api()
if cambioUSD:
    print("Cambio USD:", cambioUSD)
else:
    print("Falha ao obter o resultado do Cambio USD.")