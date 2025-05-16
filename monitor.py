import requests
from datetime import datetime

# Lista de sites a serem monitorados
sites = [
     ("https://www.pasqualisolution.com.br/")
]

def verificar_site(url):
    try:
        resposta = requests.get(url, timeout=5)
        status = resposta.status_code
        if status == 200:
            return f"[{datetime.now()}]  {url} está ONLINE"
        else:
            return f"[{datetime.now()}]  {url} respondeu com status {status}"
    except requests.exceptions.RequestException:
        return f"[{datetime.now()}]  {url} está OFFLINE"

# Rodar verificações
for site in sites:
    print(verificar_site(site))
