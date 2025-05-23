import requests
import time

def verificar_site(url):
    
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        inicio = time.time()
        resposta = requests.get(url, timeout=5)
        fim = time.time()
        tempo_resposta = round(fim - inicio, 2)

        if resposta.status_code == 200:
            print(f"O site {url} está ONLINE: {tempo_resposta}s)")
        else:
            print(f"O site {url} respondeu com código: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"O site {url} está OFFLINE ")
        print(f"Detalhes do erro: {e}")

if __name__ == "__main__":
    site = input("Digite o site ou IP : ")
    verificar_site(site)


