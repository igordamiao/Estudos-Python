# pip3 install requests https://docs.python.org/3/library/index.html, https://docs.python.org/3/library/index.html e https://pypi.org/

print("\Importação e uso de um módulo terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")