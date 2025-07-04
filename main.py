import requests
from bs4 import BeautifulSoup

def coletar_manchetes_g1():
    url = 'https://g1.globo.com/'
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print(f"Erro ao acessar o site. Código: {resposta.status_code}")
        return []

    soup = BeautifulSoup(resposta.text, 'html.parser')

    # As manchetes estão nas tags <a> com classe 'feed-post-link'
    manchetes_tags = soup.find_all('a', class_='feed-post-link')
    
    manchetes = [tag.get_text(strip=True) for tag in manchetes_tags]

    return manchetes

if __name__ == "__main__":
    print("Coletando manchetes do G1...\n")
    manchetes = coletar_manchetes_g1()
    
    for i, m in enumerate(manchetes[:10], start=1):
        print(f"{i}. {m}")
