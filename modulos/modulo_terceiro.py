# pip3 install requests

print("\Importação e uso de um módulo terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")