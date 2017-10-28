from bs4 import BeautifulSoup
from urllib import urlopen

url = 'http://seti.ufla.br'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

texto = soup.find('p').text

print(texto)