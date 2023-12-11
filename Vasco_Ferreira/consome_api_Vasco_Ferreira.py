import requests
request = requests.get('http://instituto.islagaia.pt/ws/wsCambio.asmx/cambioUSD')
print(request.text)	
