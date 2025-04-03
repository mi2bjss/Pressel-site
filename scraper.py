import requests
from bs4 import BeautifulSoup

url = "https://pt.triumph.com/"  # Altere para o site desejado

# Faz a requisição HTTP
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.text

# Processa o HTML com BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Exemplo: pega o título da página
title = soup.title.text
print("Título da página:", title)

import requests
from bs4 import BeautifulSoup

# Novo código para extrair links com BeautifulSoup
url = "https://pt.triumph.com/"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.text

soup = BeautifulSoup(html, "html.parser")

# Extraindo todos os links da página
links = soup.find_all('a')  # encontra todas as tags <a>

# Exibindo os links
for link in links:
    href = link.get('href')  # Pegando o atributo 'href' de cada tag <a>
    if href:
        print(href)

