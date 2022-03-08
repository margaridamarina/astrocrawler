from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def request():
  response = urlopen('https://astrojourney.com.br/blog/')
  html = response.read().decode('utf-8')
  soup = BeautifulSoup(html, 'html.parser')
  return soup

def extract_links(soup):
  titulos = soup.select("article div h5 a")
  lista_links = []
  for link in titulos:
      lista_links.append(link.get('href'))
  return lista_links

def request_html_from_links(lista_links):
  lista_html = []
  for item in lista_links: 
      response = urlopen(item)
      html = response.read().decode('utf-8')
      lista_html.append(html)
  return lista_html

def extract_data(lista_html):
  lista_titulos = []
  for html in lista_html: 
      soup = BeautifulSoup(html, 'html.parser')
      titulos = soup.select("div div div h2")
      for titulo in titulos:
          lista_titulos.append(titulo.get_text())

  lista_conteudo = []
  for html in lista_html: 
      soup = BeautifulSoup(html, 'html.parser')
      conteudo = soup.find("div", {"class": "post_text_inner"})
      # lista_conteudo.append(conteudo.get_text().replace('\n', '').replace('\t', '').strip()) 
      lista_conteudo.append(conteudo.get_text().strip())
  dicionario = dict(zip(lista_titulos, lista_conteudo))
  return dicionario

if __name__ == '__main__':
  soup = request()
  lista_links = extract_links(soup)
  lista_html = request_html_from_links(lista_links)
  dicionario = extract_data(lista_html)
  with open('Posts.json', 'w') as f:
    json.dump(dicionario, f, ensure_ascii=False, indent=4)