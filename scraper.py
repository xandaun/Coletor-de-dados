import requests
from bs4 import BeautifulSoup

def coletar_manchetes_g1():
    url = 'https://g1.globo.com/'
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return ["Erro ao acessar o G1."]

    soup = BeautifulSoup(resposta.text, 'html.parser')
    manchetes_tags = soup.find_all('a', class_='feed-post-link')
    manchetes = [tag.get_text(strip=True) for tag in manchetes_tags]

    return manchetes[:10]
